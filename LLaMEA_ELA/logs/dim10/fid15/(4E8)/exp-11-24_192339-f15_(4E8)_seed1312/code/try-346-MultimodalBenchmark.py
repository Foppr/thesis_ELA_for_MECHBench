import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum system parameters
        self.hbar = 1.0
        self.omega = 2.0
        self.alpha = 0.5
        self.beta = 0.3
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum superposition component with entanglement
        quantum_superposition = 0
        for i in range(self.dim):
            # Wavefunction amplitude with quantum interference
            amp1 = np.exp(-0.5 * (x[i] - self.alpha)**2) * np.cos(self.omega * x[i])
            amp2 = np.exp(-0.5 * (x[i] + self.alpha)**2) * np.sin(self.omega * x[i])
            quantum_superposition += (amp1 + amp2)**2
            
        # Dynamic phase interference pattern with chaotic modulation
        phase_interference = 0
        for i in range(self.dim):
            # Time-varying phase with adaptive coupling and chaotic modulation
            chaotic_mod = np.sin(0.5 * x[i] + self.dim * 0.2 + np.sin(x[i] * 0.3))
            phase = self.beta * np.sin(0.5 * x[i] + self.dim * 0.2) * np.cos(0.3 * x[i]) * chaotic_mod
            phase_interference += np.sin(x[i] + phase)**2
            
        # Adaptive energy basin with fractal characteristics and quantum tunneling effect
        energy_basin = 0
        for i in range(self.dim):
            # Basin depth varies with dimension and input, with fractal scaling
            depth = 1.5 + 0.4 * np.sin(0.7 * x[i] + self.dim * 0.3) + 0.2 * np.sin(3 * x[i])
            energy_basin += depth * (x[i]**2 - 2 * x[i] + 1) * np.exp(-0.2 * x[i]**2)
            
        # Cross-dimensional quantum entanglement with fractal correlation
        entanglement = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Quantum correlation coefficient with fractal modulation
                corr = 0.6 + 0.4 * np.sin(0.4 * (x[i] + x[j]) + self.dim * 0.15 + 
                                        0.3 * np.sin(x[i] * 0.5))
                entanglement += corr * np.sin(x[i] - x[j])**2 * np.cos(x[i] + x[j])**2
                
        # Quantum tunneling probability landscape with fractal potential
        tunneling = 0
        for i in range(self.dim):
            # Tunneling probability with quantum potential and fractal scaling
            pot = 0.8 * np.exp(-0.3 * (x[i] - 1)**2) + 0.5 * np.exp(-0.4 * (x[i] + 1)**2)
            fractal_pot = pot + 0.1 * np.sin(5 * x[i]) * np.cos(2 * x[i])
            tunneling += np.exp(-fractal_pot) * np.sin(2 * x[i])**2
            
        # Fractal dimensionality scaling component
        fractal_scaling = 0
        for i in range(self.dim):
            fractal_scaling += (1 + 0.3 * np.sin(x[i] * 0.7)) * np.log(1 + np.abs(x[i]))
            
        # Final quantum landscape combining all components with chaotic mixing
        return (0.25 * quantum_superposition + 0.2 * phase_interference + 
                0.25 * energy_basin + 0.15 * entanglement + 0.1 * tunneling + 
                0.05 * fractal_scaling)