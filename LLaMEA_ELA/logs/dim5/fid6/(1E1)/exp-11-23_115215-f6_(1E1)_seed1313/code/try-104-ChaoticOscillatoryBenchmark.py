import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute oscillation frequencies and chaotic parameters
        self.frequencies = np.linspace(1.0, 15.0, dim)
        self.chaotic_params = np.random.uniform(3.5, 4.0, dim)
        self.harmonic_coeffs = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with chaotic modulation
        base_val = np.sum(x**2) * (1.0 + 0.3 * np.sin(np.sum(x) * 0.7))
        
        # Spherical harmonics with varying degrees and orders
        f_val = base_val
        for i in range(self.dim):
            harmonic = self.harmonic_coeffs[i] * np.sin(i * np.pi / (self.dim + 1)) * \
                      np.cos(i * np.pi / (self.dim + 1))
            f_val += 0.6 * harmonic * np.exp(-0.1 * x[i]**2)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.4 * np.sin(self.frequencies[i] * x[i]) * \
                     np.cos(self.frequencies[i] * x[i] * 0.3) + \
                     0.2 * np.sin(self.frequencies[i] * x[i] * 2.0)
        
        # Radial basis functions with dynamic centers and widths
        for i in range(self.dim):
            center = 2.5 * np.sin(i * 0.5 + np.sum(x) * 0.15)
            width = 0.3 + 0.7 * np.cos(i * 0.4)
            f_val += 0.5 * np.exp(-0.5 * ((x[i] - center) / width)**2) * \
                     (1.0 + 0.15 * np.sin(i * 0.8))
        
        # Chaotic perturbations using logistic maps with feedback
        chaotic_sum = 0.0
        for i in range(self.dim):
            if i == 0:
                chaotic_val = x[i]
            else:
                chaotic_val = self.chaotic_params[i] * x[i-1] * (1 - x[i-1])
            
            f_val += 0.25 * np.sin(chaotic_val * 12 + i) * \
                     np.cos(chaotic_val * 8 + i)
            chaotic_sum += chaotic_val
        
        # Coupling terms with exponential decay and harmonic modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling = np.exp(-0.4 * (j - i)) * np.sin(x[i] + x[j])
                f_val += 0.3 * coupling * (x[i]**2 + x[j]**2) * \
                         np.cos(0.5 * (i + j))
        
        # High-order polynomial interactions with chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.15 * (x[i]**4) * (x[j]**2) + \
                         0.08 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * \
                         np.exp(-0.1 * np.abs(x[i] - x[j]))
        
        # Asymmetric cross-terms with chaotic modulation
        for i in range(self.dim):
            if i > 0:
                diff = x[i] - x[i-1]
                f_val += 0.25 * (diff**4 + 0.4 * np.abs(diff)**3) + \
                         0.15 * np.sin(x[i]) * np.cos(x[i-1]) * \
                         np.exp(-0.05 * np.abs(x[i] - x[i-1]))
        
        # Final chaotic modulation with global interaction
        f_val += 0.4 * np.sin(np.sum(np.sin(x))) + \
                 0.2 * np.cos(np.prod(np.cos(x))) + \
                 0.15 * np.sin(np.sum(np.abs(x)) * 0.6) + \
                 0.1 * np.exp(-0.2 * np.sum(np.abs(x)))
        
        # Add a global harmonic term
        f_val += 0.3 * np.cos(np.sum(x) * 0.5) * np.sin(np.sum(np.cos(x))) * \
                 np.exp(-0.05 * np.sum((x - 1.0)**2))
        
        return f_val