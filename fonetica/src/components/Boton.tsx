interface Props {
    href: string;
    label: string;
  }


export default function Boton({label, href}: Props) {
    return (
        <button className="rounded-lg bg-usach-daisy-900">
            <a href={href}>    
                    {label}
            </a>
        </button>
    )
}