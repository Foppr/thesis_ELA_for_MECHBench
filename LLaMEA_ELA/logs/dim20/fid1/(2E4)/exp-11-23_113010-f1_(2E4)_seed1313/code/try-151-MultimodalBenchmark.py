import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        # Fractal structure with recursive scaling
        for i in range(self.dim):
            # Power-law scaling with fractal dimension
            scale_factor = np.power(np.abs(x_norm[i]) + 1e-8, 0.42)
            
            # Sinusoidal components with multi-scale frequencies
            freq1 = 2 * np.pi * (i + 1) * (1 + 0.6 * np.sin(x_norm[i] * np.pi / 2))
            freq2 = 3 * np.pi * (i + 1) * (1 + 0.4 * np.cos(x_norm[i] * np.pi / 3))
            
            # Recursive dimension coupling with chaotic logistic map
            coupling = 1.0
            for j in range(i):
                # Time-delayed feedback with logistic chaos
                delay_term = 0.1 * np.sin(x_norm[j] * (j + 1) * np.pi / (i + 1)) * (1 - x_norm[j]**2)
                coupling *= (1 + 0.15 * delay_term)
            
            # Multi-scale sinusoidal modulation with chaotic perturbation
            term1 = np.sin(freq1 * x_norm[i]) * np.cos(freq2 * x_norm[i])
            term2 = np.sin(freq1 * x_norm[i]**2) * np.cos(freq2 * x_norm[i]**3)
            
            # Add chaotic logistic modulation
            chaos_mod = 0.05 * (1 - x_norm[i]**2) * np.sin(10 * x_norm[i])
            
            # Combine with power-law scaling and coupling
            result += scale_factor * coupling * (term1 + 0.6 * term2 + chaos_mod)
        
        # Add self-similar fractal component with delayed feedback
        fractal_component = 0.0
        for i in range(self.dim):
            # Recursive pattern with decreasing amplitude and delay
            amp = 0.12 / (i + 1)
            freq = 2**(i % 5 + 1) * (1 + 0.3 * np.sin(i * np.pi / self.dim))
            # Add time-delayed chaotic component
            delay_feedback = 0.08 * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**2) * (1 - x_norm[i-1]**2 if i > 0 else 0)
            fractal_component += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**2) + delay_feedback
        
        # Combine main and fractal components with dynamic weighting
        weight_main = 0.55 + 0.45 * np.sin(self.dim * 0.25)
        weight_fractal = 0.45 + 0.55 * np.cos(self.dim * 0.18)
        
        return weight_main * result + weight_fractal * fractal_component