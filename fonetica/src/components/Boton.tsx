interface Props {
    href: string;
    label: string;
    type?: string;
}
  
export default function Boton({ label, href, type }: Props) {
    return (
        <button className="rounded-lg bg-usach-daisy-800 hover:bg-usach-daisy-900 p-2" itemType={type}>
            <a href={href}>{label}</a>
        </button>
    );
}