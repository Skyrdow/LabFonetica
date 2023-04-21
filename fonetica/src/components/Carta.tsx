interface Props {
    title: string;
    description?: string;
  }

export default function Carta({ title, description }: Props) {
    return (
        <div className="rounded-lg bg-usach-terra-800 p-4 text-xl">
            <h1>{title}</h1>
            <p>{description}</p>
        </div>
    );
}