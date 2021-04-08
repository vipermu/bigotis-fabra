<script lang="typescript">
	import router from "page";
	import Environments from "./routes/Environments.svelte";
	import Launch from "./routes/Launch.svelte";

	let page;

	router("/", () => (page = Environments));
	router("environments", () => (page = Launch));
	router.start();
</script>

<!-- <svelte:component this={Environments} /> -->
<Environments />
