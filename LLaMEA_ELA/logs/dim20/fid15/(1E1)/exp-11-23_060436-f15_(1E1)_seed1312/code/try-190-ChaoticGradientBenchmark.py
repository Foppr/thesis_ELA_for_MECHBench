import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2) * 0.1
        
        # Periodic peak component with dynamic frequencies and amplitudes
        peaks = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * i)
            amp = 1.0 + 0.5 * np.cos(0.4 * i)
            peak_loc = 2.0 * np.sin(0.5 * i)
            peaks += amp * np.exp(-0.5 * ((x[i] - peak_loc) / (0.5 + 0.3 * np.sin(0.2 * i)))**2) * np.cos(freq * x[i])
        
        # Gaussian valley component with dynamic locations and widths
        valleys = 0
        for i in range(self.dim):
            valley_loc = 1.5 * np.cos(0.4 * i)
            width = 0.8 + 0.4 * np.sin(0.3 * i)
            valleys += -0.5 * np.exp(-0.5 * ((x[i] - valley_loc) / width)**2) * (1.0 + 0.3 * np.cos(0.2 * i))
        
        # Dynamic conditioning component with varying curvature
        conditioning = 0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.8 * np.sin(0.5 * i) * np.cos(0.3 * i)
            conditioning += cond_factor * x[i]**4
        
        # Cross-dimensional interaction with periodic modulation
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 0.5 + 0.3 * np.sin(0.2 * (i + j))
                interaction += weight * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Multi-scale oscillation with varying frequencies and amplitudes
        oscillation = 0
        for i in range(self.dim):
            freqs = [1.0, 2.0, 3.0, 4.0]
            scale_idx = i % len(freqs)
            freq = freqs[scale_idx]
            amp = 0.8 + 0.4 * np.sin(0.3 * i)
            oscillation += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Chaotic modulation with logistic map behavior
        chaotic_mod = 0
        for i in range(self.dim):
            r = 3.8 + 0.2 * np.sin(0.4 * i)
            x_prev = x[i-1] if i > 0 else x[0]
            logistic = r * x_prev * (1 - x_prev)
            chaotic_mod += logistic * np.exp(-0.1 * x[i]**2)
        
        # Asymmetric component with different behavior in positive and negative domains
        asymmetric = 0
        for i in range(self.dim):
            asym_factor = 1.0 + 0.5 * np.sin(0.3 * i)
            if x[i] >= 0:
                asymmetric += asym_factor * np.sin(x[i]) * np.exp(-0.2 * x[i]**2)
            else:
                asymmetric += asym_factor * np.cos(x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Combined fitness function with optimized weights
        return (quadratic * 0.6 +
                peaks * 0.4 +
                valleys * 0.3 +
                conditioning * 0.25 +
                interaction * 0.2 +
                oscillation * 0.35 +
                chaotic_mod * 0.18 +
                asymmetric * 0.2)