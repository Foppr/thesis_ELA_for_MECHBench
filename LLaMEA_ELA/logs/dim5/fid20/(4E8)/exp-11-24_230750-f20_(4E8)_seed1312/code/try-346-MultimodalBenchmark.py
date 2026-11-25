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
            freq = 3.0 + 2.0 * np.sin(0.4 * x[i] + 1.0)
            amp = 1.5 + 1.0 * np.cos(0.6 * x[i]**2 + 0.5)
            phase = 0.3 * np.sin(1.2 * x[i])
            wave_interference += amp * np.sin(freq * x[i] + phase) * np.exp(-0.1 * np.abs(x[i]))
        
        # Asymmetric Gaussian clusters with dynamic center and variance
        gaussian_clusters = 0.0
        for i in range(self.dim):
            for j in range(4):
                center = -4.0 + 2.0 * j + 0.8 * np.sin(0.7 * x[i] + 0.3)
                variance = 1.0 + 0.5 * np.cos(0.5 * x[i]) * np.sin(0.4 * x[i]**2)
                asymmetry = 1.2 + 0.4 * np.sin(0.6 * x[i] + 0.2)
                gaussian_clusters += asymmetry * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Harmonic potential with adaptive stiffness and cross-dimensional coupling
        harmonic_potential = 0.0
        for i in range(self.dim):
            stiffness = 1.5 + 0.8 * np.sin(0.8 * x[i]) * np.cos(0.5 * x[i])
            harmonic_potential += 0.5 * stiffness * x[i]**2
        
        # Cross-dimensional coupling with sinusoidal interaction weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = np.sin(0.3 * (x[i] - x[j])**2 + 0.1)
                coupling += weight * (x[i]**2 + x[j]**2) * np.cos(0.6 * (x[i] + x[j]))
        
        # Multi-scale oscillatory structure with complex phase shifts
        multi_scale = 0.0
        for i in range(self.dim):
            scale_factor = 1.5 + 0.7 * np.sin(1.0 * x[i] + 0.4)
            multi_scale += scale_factor * np.sin(4.0 * x[i] + 0.7 * np.cos(3.0 * x[i]))
        
        # Dimensionally adaptive normalization factor with exponential scaling
        norm_factor = 1.2 + 0.3 * np.log(self.dim + 2) * np.exp(-0.05 * self.dim)
        
        return (0.28 * wave_interference + 0.27 * gaussian_clusters + 
                0.22 * harmonic_potential + 0.18 * coupling + 0.05 * multi_scale) * norm_factor