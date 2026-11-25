import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potential wells with varying depths
        pot_energy = 0
        for i in range(self.dim):
            pot_energy += np.exp(-0.5 * (x[i] / 2.0)**2) * (1.0 + 0.5 * np.sin(3.0 * x[i]))
        
        # Sine-wave modulation with spatially varying frequencies and amplitudes
        wave_mod = 0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.cos(0.5 * i)
            amp = 0.8 + 0.2 * np.sin(0.7 * i)
            wave_mod += amp * np.sin(freq * x[i] + 0.2 * i) * np.cos(freq * x[i] / 2.0 + 0.1 * i)
        
        # Radial symmetry component with multiple peaks and valleys
        radial_sym = 0
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            radial_sym = np.sin(5.0 * r) * np.exp(-0.1 * r) + 0.3 * np.cos(3.0 * r)
        
        # Cross-dimensional coupling with quadratic interaction terms
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                cross_coupling += 0.2 * diff**2 * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Additional noise-like perturbation to increase ruggedness
        noise = 0
        for i in range(self.dim):
            noise += 0.1 * np.sin(7.0 * x[i]) * np.cos(4.0 * x[i])
        
        # Combine all components with appropriate scaling factors
        return 1.5 * pot_energy + 1.2 * wave_mod + 0.8 * radial_sym + 0.6 * cross_coupling + 0.3 * noise + 2.0 * self.dim