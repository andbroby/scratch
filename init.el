(add-to-list 'load-path "~/.emacs.d/el-get/el-get")

(unless (require 'el-get nil 'noerror)
    (with-current-buffer
            (url-retrieve-synchronously
	             "https://raw.githubusercontent.com/dimitri/el-get/master/el-get-install.el")
	        (goto-char (point-max))
		    (eval-print-last-sexp)))

(add-to-list 'el-get-recipe-path "~/.emacs.d/el-get-user/recipes")
(el-get 'sync)

(require 'evil)
(evil-mode 1)
(define-key evil-normal-state-map (kbd "SPC") 'ace-jump-mode)


(global-linum-mode t)
(setq linum-format "%4d \u2502 ")

(add-to-list 'default-frame-alist '(left-fringe . 11))
(add-to-list 'default-frame-alist '(right-fringe . 0))

(setq mac-option-modifier nil
      mac-command-modifier 'meta
      x-select-enable-clipboard t)

(add-hook 'python-mode-hook
	  'jedi:setup
	  (lambda ()
	    (setq jedi:complete-on-dot t)
	    (setq indent-tabs-mode t)
	    (setq tab-width 4)
	    (setq python-indent 4)))

(when (memq window-system '(mac ns))
  (exec-path-from-shell-initialize))

(setq locale-coding-system 'utf-8)
(set-terminal-coding-system 'utf-8)
(set-keyboard-coding-system 'utf-8)
(set-selection-coding-system 'utf-8)
(prefer-coding-system 'utf-8)

(defun rename-file-and-buffer (new-name)
  "Renames both current buffer and file it's visiting to NEW-NAME."
  (interactive "sNew name: ")
  (let ((name (buffer-name))
        (filename (buffer-file-name)))
    (if (not filename)
        (message "Buffer '%s' is not visiting a file!" name)
      (if (get-buffer new-name)
          (message "A buffer named '%s' already exists!" new-name)
        (progn
          (rename-file name new-name 1)
          (rename-buffer new-name)
          (set-visited-file-name new-name)
          (set-buffer-modified-p nil))))))

(setq mac-command-modifier 'meta)
(setq mac-option-modifier nil)

(load-file "~/.emacs.d/themes/zenburn.el")
