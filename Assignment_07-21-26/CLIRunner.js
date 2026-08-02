// runner.js - fixed version
class ConfigError extends Error {
    constructor(message) {
        super(message);
        this.name = 'ConfigError';
    }
}

function loadThreshold() {
    const value = process.env.MAX_ITEMS;

    if (!value) {
        throw new ConfigError("MAX_ITEMS is missing");
    }

    return Number(value);
}

async function run(items) {
    const limit = loadThreshold();

    if (items.length > limit) {
        throw new Error(`Too many items: ${items.length} > ${limit}`);
    }

    return items.map(i => i.toUpperCase());
}

const verbose = process.argv.includes('--verbose');


process.on("unhandledRejection", (err) => {
    console.error("Unhandled Rejection:", err);
});

(async () => {
    try {
        if (!process.env.MAX_ITEMS) {
            process.env.MAX_ITEMS = "10"; // Default value
            console.log('ℹ️ MAX_ITEMS not set, using default: 10');
        }
        
        const result = await run(["Piatos", "Fudgee Bar", "Coke"]);
        console.log(result);
    } catch (err) {
        if (verbose) {
            console.error(err.stack);
        } else {
            console.error(err.message);
        }
    }
})();