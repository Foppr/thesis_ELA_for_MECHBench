import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Hyperchaotic component with multiple logistic maps
        chaotic_term = 0
        r_values = [3.8, 3.9, 3.95, 4.0]
        for i in range(self.dim):
            logistic_val = 0
            for r in r_values:
                logistic_val += r * x_norm[i] * (1 - x_norm[i])
            chaotic_term += logistic_val * np.sin(15 * x_norm[i]) * np.cos(8 * x_norm[i])
        
        # Fractional Brownian motion inspired modulation
        fbm_term = 0
        hurst = 0.7
        for i in range(self.dim):
            fbm_val = np.sin(x_norm[i] ** (1 + hurst)) * np.cos(x_norm[i] ** (2 - hurst))
            fbm_term += fbm_val * np.sin(3 * x_norm[i]) * np.cos(5 * x_norm[i])
        
        # Quantum-inspired basin structures with superposition states
        basin_term = 0
        for i in range(self.dim):
            # Superposition of multiple quadratic wells
            well1 = (x_norm[i] - 0.3)**2 + 0.1
            well2 = (x_norm[i] + 0.4)**2 + 0.05
            well3 = x_norm[i]**2 + 0.2
            basin_term += min(well1, well2, well3) * np.sin(2 * x_norm[i])
        
        # Extended cross-dimensional coupling with fractal interaction
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Even more extended coupling
                # Fractal coupling strength based on distance
                dist = np.abs(i - j)
                coupling_strength = 3.0 / (1 + 0.1 * dist**1.5)
                # Fractal interaction term with multiple harmonics
                fractal_interaction = np.sin(x_norm[i] + x_norm[j]) * np.cos(2*x_norm[i] - x_norm[j])
                fractal_interaction += 0.5 * np.sin(3*x_norm[i] + 2*x_norm[j]) * np.cos(x_norm[i] + 3*x_norm[j])
                fractal_interaction += 0.3 * np.sin(4*x_norm[i] - x_norm[j]) * np.cos(2*x_norm[i] + 4*x_norm[j])
                cross_term += coupling_strength * (x_norm[i]**2) * (x_norm[j]**2) * fractal_interaction
        
        # Multi-scale phase modulation with quantum interference
        phase_term = 0
        for i in range(self.dim):
            phase_shift1 = np.pi * (i % 5) / 5
            phase_shift2 = np.pi * ((i * 4) % 6) / 6
            phase_shift3 = np.pi * ((i * 7) % 8) / 8
            phase_term += np.sin(3 * x_norm[i] + phase_shift1) * np.cos(4 * x_norm[i] + phase_shift2) * np.sin(2 * x_norm[i] + phase_shift3)
        
        # Ultra-high frequency harmonic resonance with quantum tunneling effect
        resonance_term = 0
        for i in range(self.dim):
            resonance_term += (np.sin(8 * x_norm[i]) + 0.7 * np.cos(12 * x_norm[i])) * \
                             (1 + 0.5 * np.sin(3 * x_norm[i])) * \
                             np.exp(-0.5 * x_norm[i]**2)
        
        # Fractal dimensionality scaling component
        fractal_dim_term = 0
        for i in range(self.dim):
            fractal_dim_term += (np.sin(10 * x_norm[i]) + np.cos(15 * x_norm[i])) * \
                               (1 + 0.3 * np.sin(5 * x_norm[i]))
        
        # Combine all components with optimized weights
        result = 2.2 * chaotic_term + 1.8 * fbm_term + 1.6 * basin_term + 1.7 * cross_term + 1.1 * phase_term + 0.9 * resonance_term + 0.8 * fractal_dim_term
        
        # Add hyperchaotic noise for maximum sensitivity
        noise = np.random.normal(0, 0.002) * (1 + 0.5 * np.sin(np.sum(x_norm)))
        
        return result + noise