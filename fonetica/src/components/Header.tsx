export default function Header() {
    return (
        <header className="bg-usach-industrial-1000 p-2 flex">
            <div className="h-40 flex flex-row gap-10">
                <button>
                    <a href="/" className="h-max">
                        <img src="/Usach SB.png" alt="Logo Usach" className="h-max"/>
                    </a>
                </button>
                <h1 className="m-auto text-3xl font-mono text-white align-middle">Recursos Virtuales para el aprendizaje del Lenguaje</h1>
            </div>
        </header>
    )
}