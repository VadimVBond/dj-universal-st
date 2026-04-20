(() => {
    const UI_KIT_KEY = "ui_kit";
    const VALID_UI_KITS = ["tailwind", "bootstrap", "flowbite", "daisyui", "preline"];
    const root = document.documentElement;

    const setActiveButtons = (kit) => {
        document.querySelectorAll(".ui-kit-switcher [data-ui-kit]").forEach((button) => {
            const isActive = button.dataset.uiKit === kit;
            button.classList.toggle("active", isActive);
            button.setAttribute("aria-pressed", String(isActive));
        });
    };

    const applyUiKit = (kit, persist = true) => {
        if (!VALID_UI_KITS.includes(kit)) {
            return;
        }
        root.setAttribute("data-ui-kit", kit);
        if (persist) {
            localStorage.setItem(UI_KIT_KEY, kit);
        }
        if (typeof switchUiKitCss === "function") {
            switchUiKitCss(kit);
        }
        setActiveButtons(kit);
    };

    document.addEventListener("DOMContentLoaded", () => {
        const saved = localStorage.getItem(UI_KIT_KEY);
        const initial = VALID_UI_KITS.includes(saved) ? saved : "tailwind";
        applyUiKit(initial, false);
        if (!VALID_UI_KITS.includes(saved)) {
            localStorage.setItem(UI_KIT_KEY, initial);
        }

        document.querySelectorAll(".ui-kit-switcher [data-ui-kit]").forEach((button) => {
            button.addEventListener("click", () => {
                applyUiKit(button.dataset.uiKit);
            });
        });
    });
})();
