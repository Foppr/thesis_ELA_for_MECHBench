import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term
        quadratic = 0.5 * np.sum(x**2) / self.dim
        
        # Enhanced fractal component with chaotic recursion
        fractal = 0.0
        for i in range(self.dim):
            val = x[i]
            # Chaotic recursive pattern with varying frequencies
            for depth in range(1, 8):
                freq = 2**depth + np.sin(depth * 0.5)
                val = np.sin(freq * val) + 0.3 * np.cos(freq * val * 1.5)
            fractal += val**2
        
        # Power-law scaling with chaotic frequency modulation
        power_law = 0.0
        for i in range(self.dim):
            freqs = [1, 2, 3, 4, 6, 8]
            scale = 1.0 / (1.0 + np.abs(x[i]))
            # Add chaotic modulation to frequencies
            for f in freqs:
                mod_freq = f * (1 + 0.2 * np.sin(f * x[i]))
                power_law += (scale**mod_freq) * np.sin(mod_freq * x[i]) * np.cos(mod_freq * x[i] * 0.3)
        
        # Multi-scale interaction with chaotic coupling
        multiscale = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.abs(x[i] - x[j])
                # Add chaotic modulation to interaction strength
                strength = np.exp(-dist**2) * (1 + 0.1 * np.sin(dist * 7))
                multiscale += strength * np.sin(12 * dist) * np.cos(6 * dist)
        
        # Self-similar ridge with chaotic amplitude modulation
        ridge = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.4 * np.sin(i * 0.8 + np.cos(i * 0.3))
            ridge += amp * np.sin(9 * x[i]) * np.cos(4.5 * x[i]) * np.exp(-0.25 * x[i]**2)
        
        # Cross-dimensional coupling with chaotic polynomial interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add chaotic modulation to coupling strength
                mod_strength = 1 + 0.3 * np.sin(i * j * 0.2)
                coupling += mod_strength * (x[i]**2 + x[j]**2)**1.7 * np.sin(x[i] * x[j]) * np.cos(0.6 * x[i] * x[j])
        
        # Noise-like perturbations with chaotic behavior and dynamic frequency
        noise = 0.0
        for i in range(self.dim):
            freq_mod = 25 + 5 * np.sin(x[i] * 0.5)
            noise += 0.12 * np.sin(freq_mod * x[i] + np.sin(freq_mod * x[i] * 0.3)) * np.cos(18 * x[i])
        
        # Final combination with optimized weights
        return quadratic + 0.9 * fractal + 0.4 * power_law + 0.6 * multiscale + 0.5 * ridge + 0.3 * coupling + noise