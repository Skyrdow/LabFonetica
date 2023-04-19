interface Props {
    title: string;
    description?: string;
  }

export default function Carta({title, description}: Props) {
    return (
        <div className="rounded-lg bg-usach-daisy-900">
            <h1>{title}</h1>
            <p>{description}</p>
        </div>
    )
}