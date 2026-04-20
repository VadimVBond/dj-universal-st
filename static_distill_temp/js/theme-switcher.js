(() => {
    const THEME_KEY = "theme_mode";
    const VALID_THEMES = ["light", "dark"];
    const root = document.documentElement;

    const setActiveThemeButtons = (mode) => {
        document.querySelectorAll("[data-theme-value]").forEach((button) => {
            const isActive = button.dataset.themeValue === mode;
            button.classList.toggle("active", isActive);
            button.setAttribute("aria-pressed", String(isActive));
        });
    };

    const syncToggleInputs = (mode) => {
        document.querySelectorAll("[data-theme-toggle='checkbox']").forEach((input) => {
            input.checked = mode === "dark";
        });
    };

    const applyTheme = (mode, persist = true) => {
        if (!VALID_THEMES.includes(mode)) {
            return;
        }
        root.setAttribute("data-theme", mode);
        if (persist) {
            localStorage.setItem(THEME_KEY, mode);
        }
        setActiveThemeButtons(mode);
        syncToggleInputs(mode);
    };

    document.addEventListener("DOMContentLoaded", () => {
        const saved = localStorage.getItem(THEME_KEY);
        const initial = VALID_THEMES.includes(saved) ? saved : "light";
        applyTheme(initial, false);
        if (!VALID_THEMES.includes(saved)) {
            localStorage.setItem(THEME_KEY, initial);
        }

        document.querySelectorAll("[data-theme-value]").forEach((button) => {
            button.addEventListener("click", () => {
                applyTheme(button.dataset.themeValue);
            });
        });

        document.querySelectorAll("[data-theme-toggle='checkbox']").forEach((input) => {
            input.addEventListener("change", () => {
                applyTheme(input.checked ? "dark" : "light");
            });
        });
    });
})();
