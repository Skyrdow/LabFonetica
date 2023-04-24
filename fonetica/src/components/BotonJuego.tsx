interface Props {
    href: string;
    label: string;
    type?: string;
}
  
export default function BotonJuego({ label, href, type }: Props) {
    return (
        <button className="rounded-lg bg-usach-terra-800 hover:bg-usach-ultra-800 text-5xl text-white my-3 drop-shadow p-4 px-8" itemType={type}>
            <a href={href}>{label}</a>
        </button>
    );
}