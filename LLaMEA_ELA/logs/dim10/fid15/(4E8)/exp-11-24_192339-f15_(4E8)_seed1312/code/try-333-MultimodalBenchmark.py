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
            
        # Dynamic phase interference pattern
        phase_interference = 0
        for i in range(self.dim):
            # Time-varying phase with adaptive coupling
            phase = self.beta * np.sin(0.5 * x[i] + self.dim * 0.2) * np.cos(0.3 * x[i])
            phase_interference += np.sin(x[i] + phase)**2
            
        # Adaptive energy basin with quantum tunneling effect
        energy_basin = 0
        for i in range(self.dim):
            # Basin depth varies with dimension and input
            depth = 1.5 + 0.4 * np.sin(0.7 * x[i] + self.dim * 0.3)
            energy_basin += depth * (x[i]**2 - 2 * x[i] + 1) * np.exp(-0.2 * x[i]**2)
            
        # Cross-dimensional quantum entanglement
        entanglement = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Quantum correlation coefficient
                corr = 0.6 + 0.4 * np.sin(0.4 * (x[i] + x[j]) + self.dim * 0.15)
                entanglement += corr * np.sin(x[i] - x[j])**2 * np.cos(x[i] + x[j])**2
                
        # Quantum tunneling probability landscape
        tunneling = 0
        for i in range(self.dim):
            # Tunneling probability with quantum potential
            pot = 0.8 * np.exp(-0.3 * (x[i] - 1)**2) + 0.5 * np.exp(-0.4 * (x[i] + 1)**2)
            tunneling += np.exp(-pot) * np.sin(2 * x[i])**2
            
        # Final quantum landscape combining all components
        return (0.3 * quantum_superposition + 0.25 * phase_interference + 
                0.2 * energy_basin + 0.15 * entanglement + 0.1 * tunneling)