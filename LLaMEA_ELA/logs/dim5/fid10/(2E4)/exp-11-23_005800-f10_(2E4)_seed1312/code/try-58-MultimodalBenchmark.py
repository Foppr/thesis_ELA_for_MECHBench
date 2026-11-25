import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay potential wells with varying depths and frequencies
        pot_energy = 0
        for i in range(self.dim):
            pot_energy += np.exp(-0.3 * (x[i] / 1.5)**2) * (1.0 + 0.7 * np.sin(4.0 * x[i]) + 0.3 * np.cos(2.0 * x[i]))
        
        # Modified sine-wave modulation with increased frequency and amplitude variations
        wave_mod = 0
        for i in range(self.dim):
            freq = 1.5 + 0.5 * np.sin(0.8 * i)
            amp = 1.0 + 0.3 * np.cos(0.6 * i)
            wave_mod += amp * np.sin(freq * x[i] + 0.3 * i) * np.cos(freq * x[i] / 3.0 + 0.2 * i)
        
        # Enhanced radial symmetry component with multiple peaks and valleys
        radial_sym = 0
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            radial_sym = np.sin(7.0 * r) * np.exp(-0.15 * r) + 0.4 * np.cos(4.0 * r) + 0.2 * np.sin(2.0 * r)
        
        # Improved cross-dimensional coupling with cubic interaction terms for increased complexity
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                cross_coupling += 0.3 * diff**3 * np.exp(-0.03 * (x[i]**2 + x[j]**2))
        
        # Additional high-frequency noise-like perturbation to increase ruggedness
        noise = 0
        for i in range(self.dim):
            noise += 0.15 * np.sin(9.0 * x[i]) * np.cos(5.0 * x[i]) + 0.05 * np.sin(12.0 * x[i])
        
        # Combine all components with appropriate scaling factors
        return 1.8 * pot_energy + 1.5 * wave_mod + 1.0 * radial_sym + 0.7 * cross_coupling + 0.4 * noise + 2.5 * self.dim