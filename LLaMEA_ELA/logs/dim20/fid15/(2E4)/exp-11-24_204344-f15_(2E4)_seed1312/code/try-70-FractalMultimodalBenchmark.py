import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive scaling
        quadratic = 0.5 * np.sum(x**2) / self.dim
        
        # Enhanced fractal component with nested chaotic recursion and dynamic exponents
        fractal = 0.0
        for i in range(self.dim):
            val = x[i]
            depth = 1
            for _ in range(6):
                val = np.sin(2**depth * val) + 0.3 * np.cos(5**depth * val) + 0.1 * np.sin(7**depth * val)
                depth += 1
                if depth > 10:
                    break
            fractal += val**2
        
        # Modified power-law scaling with multi-frequency harmonic combinations and dynamic exponents
        power_law = 0.0
        for i in range(self.dim):
            freqs = [1, 3, 5, 7, 11, 13, 17]
            scale = 1.0 / (1.0 + np.abs(x[i]))
            for f in freqs:
                power_law += (scale**(f*0.4)) * np.sin(f * x[i]) * np.cos(f * x[i] * 0.3) * np.sin(f * x[i] * 0.7)
        
        # Multi-scale interaction with dynamic coupling strength and phase shifts
        multiscale = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                dist = np.abs(x[i] - x[j])
                strength = 1.0 + 0.3 * np.sin(i * 0.7) * np.cos(j * 0.5)
                multiscale += strength * np.exp(-dist**2) * np.sin(15 * dist) * np.cos(7 * dist) * (1 + 0.2 * np.sin(dist))
        
        # Adaptive ridge structure with time-varying amplitude and complex frequency combinations
        ridge = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.6) * np.cos(i * 0.4) * np.sin(i * 0.2)
            ridge += amp * np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.1 * x[i]**2) * np.cos(3 * x[i])
        
        # Enhanced cross-dimensional coupling with non-linear interaction and asymmetric scaling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i]**2 + x[j]**2)**1.5 * np.sin(x[i] * x[j]) * np.cos(0.7 * x[i] * x[j])
                asymmetry = 1.0 + 0.15 * np.sin(i + j) * np.cos(i - j)
                coupling += interaction * asymmetry
        
        # Chaotic noise with nested period-doubling and amplitude modulation
        noise = 0.0
        for i in range(self.dim):
            modulator = np.sin(25 * x[i] + np.sin(12 * x[i]) + 0.5 * np.sin(6 * x[i]))
            noise += 0.2 * np.sin(25 * x[i] + modulator) * np.cos(20 * x[i] + 0.3 * np.sin(8 * x[i])) * (1 + 0.1 * np.cos(15 * x[i]))
        
        # Additional high-frequency chaotic component
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += 0.1 * np.sin(50 * x[i]) * np.cos(30 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Final scaling and combination with dynamic weights
        return quadratic + 1.1 * fractal + 0.4 * power_law + 0.7 * multiscale + 0.5 * ridge + 0.3 * coupling + 0.25 * noise + 0.15 * high_freq