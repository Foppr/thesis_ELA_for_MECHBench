import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced periodic wave interference with chaotic modulation
        wave_interference = 0.0
        for i in range(self.dim):
            freq = 2.8 + 2.7 * np.sin(0.6 * x[i] + 1.2)
            amp = 2.2 + 1.3 * np.cos(0.8 * x[i]**2 + 0.6)
            phase = 0.5 * np.sin(1.7 * x[i])
            wave_interference += amp * np.sin(freq * x[i] + phase) * np.exp(-0.18 * np.abs(x[i]))
        
        # Asymmetric Gaussian clusters with dynamic center and variance
        gaussian_clusters = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = -4.2 + 3.2 * j + 1.0 * np.sin(0.9 * x[i] + 0.5)
                variance = 1.1 + 0.7 * np.cos(0.7 * x[i]) * np.sin(0.6 * x[i]**2)
                asymmetry = 1.4 + 0.4 * np.sin(0.8 * x[i] + 0.4)
                gaussian_clusters += asymmetry * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Harmonic potential with adaptive stiffness and cross-dimensional coupling
        harmonic_potential = 0.0
        for i in range(self.dim):
            stiffness = 1.8 + 1.2 * np.sin(1.0 * x[i]) * np.cos(0.5 * x[i])
            harmonic_potential += 0.5 * stiffness * x[i]**2
        
        # Cross-dimensional coupling with sinusoidal interaction weights (mutated)
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = np.sin(0.3 * (x[i] - x[j])**2 + 0.3)  # Changed frequency and phase
                coupling += weight * (x[i]**2 + x[j]**2) * np.cos(0.6 * (x[i] + x[j]))
        
        # Multi-scale oscillatory structure with complex phase shifts
        multi_scale = 0.0
        for i in range(self.dim):
            scale_factor = 1.8 + 0.9 * np.sin(1.3 * x[i] + 0.6)
            multi_scale += scale_factor * np.sin(3.2 * x[i] + 0.7 * np.cos(2.3 * x[i]))
        
        # Dimensionally adaptive normalization factor with exponential scaling
        norm_factor = 1.4 + 0.3 * np.log(self.dim + 4) * np.exp(-0.07 * self.dim)
        
        return (0.32 * wave_interference + 0.27 * gaussian_clusters + 
                0.23 * harmonic_potential + 0.16 * coupling + 0.02 * multi_scale) * norm_factor