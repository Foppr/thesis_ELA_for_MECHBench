import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic wave interference component with varying frequencies and amplitudes
        wave_interference = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.5 * x[i])
            amp = 1.0 + 0.7 * np.cos(0.3 * x[i]**2)
            wave_interference += amp * np.sin(freq * x[i] + 0.4 * np.sin(2.0 * x[i]))
        
        # Asymmetric Gaussian clusters with position and variance modulation
        gaussian_clusters = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = -3.0 + 2.0 * j + 0.5 * np.sin(0.6 * x[i])
                variance = 0.8 + 0.4 * np.cos(0.4 * x[i]) * np.sin(0.3 * x[i]**2)
                asymmetry = 1.0 + 0.3 * np.sin(0.5 * x[i])
                gaussian_clusters += asymmetry * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Harmonic potential with dimensionally varying stiffness coefficients
        harmonic_potential = 0.0
        for i in range(self.dim):
            stiffness = 1.0 + 0.5 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[i])
            harmonic_potential += 0.5 * stiffness * x[i]**2
        
        # Cross-dimensional coupling with exponential interaction weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = np.exp(-0.1 * (x[i] - x[j])**2)
                coupling += weight * (x[i]**2 + x[j]**2) * np.cos(0.5 * (x[i] + x[j]))
        
        # Multi-scale oscillatory structure with adaptive phase shifts
        multi_scale = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.6 * np.sin(0.8 * x[i])
            multi_scale += scale_factor * np.sin(3.0 * x[i] + 0.5 * np.cos(2.0 * x[i]))
        
        # Dimensionally adaptive normalization factor
        norm_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return (0.3 * wave_interference + 0.25 * gaussian_clusters + 
                0.2 * harmonic_potential + 0.15 * coupling + 0.1 * multi_scale) * norm_factor