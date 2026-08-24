import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum-like interference term with phase coupling
        quantum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Local coupling
                phase_diff = np.abs(x_norm[i] - x_norm[j])
                quantum += np.sin(15 * phase_diff) * np.cos(7 * phase_diff) * np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Time-delayed chaotic dynamics with memory effects
        chaotic = 0.0
        for i in range(self.dim):
            if i > 0:
                delay_term = np.sin(x_norm[i] + 0.5 * x_norm[i-1]) * np.exp(-0.3 * (x_norm[i] - x_norm[i-1])**2)
                chaotic += delay_term
            chaotic += np.sin(3 * x_norm[i])**2 * np.exp(-0.1 * x_norm[i]**2)
        
        # Adaptive ridge structure with variable curvature
        ridge = 0.0
        for i in range(self.dim):
            # Variable ridge height based on dimension
            ridge_height = 1.0 + 0.5 * np.sin(0.5 * i)
            ridge += ridge_height * (x_norm[i]**2 - 0.5)**2
        
        # Frequency-modulated wave with amplitude modulation
        wave = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4)  # Different frequency pattern
            amp_mod = 1.0 + 0.3 * np.sin(0.3 * i)
            wave += amp_mod * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.7) * np.exp(-0.2 * x_norm[i]**2)
        
        # Radial component with multiple harmonic frequencies
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2) * (np.sin(3 * r) + 0.5 * np.sin(7 * r) + 0.3 * np.sin(11 * r))
        
        # Cross-dimensional coupling with exponential interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.exp(-2 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(5 * x_norm[i] * x_norm[j])
        
        # Combine all components with adaptive weights
        return 0.2 * quantum + 0.3 * chaotic + 0.15 * ridge + 0.2 * wave + 0.1 * radial + 0.05 * coupling + 1.0