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
            # More chaotic recursive pattern
            for depth in range(1, 8):
                val = np.sin(2**depth * val) + 0.3 * np.cos(5**depth * val) + 0.1 * np.sin(7**depth * val)
            fractal += val**2
        
        # Modified power-law scaling with harmonic frequencies
        power_law = 0.0
        for i in range(self.dim):
            freqs = [1, 3, 5, 7, 11]
            scale = 1.0 / (1.0 + np.abs(x[i]))
            for f in freqs:
                power_law += (scale**(f*0.5)) * np.sin(f * x[i]) * np.cos(f * x[i] * 0.3)
        
        # Enhanced multi-scale interaction terms
        multiscale = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.abs(x[i] - x[j])
                multiscale += np.exp(-dist**2) * np.sin(15 * dist) * np.cos(7 * dist) * (1 + 0.2 * np.sin(dist))
        
        # Adaptive ridge structure with dynamic amplitude
        ridge = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.4 * np.sin(i * 0.5) * np.cos(i * 0.3)
            ridge += amp * np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Improved cross-dimensional coupling with asymmetric interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i]**2 + x[j]**2)**1.3 * np.sin(x[i] * x[j]) * np.cos(0.7 * x[i] * x[j])
                coupling += interaction * (1 + 0.1 * np.sin(i + j))
        
        # Chaotic noise with period-doubling behavior
        noise = 0.0
        for i in range(self.dim):
            noise += 0.15 * np.sin(25 * x[i] + np.sin(12 * x[i]) + 0.5 * np.sin(6 * x[i])) * np.cos(20 * x[i])
        
        # Additional chaotic modulation for improved discrimination
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += 0.2 * np.sin(3 * x[i]) * np.cos(7 * x[i]) * np.sin(11 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Final scaling and combination
        return quadratic + 0.9 * fractal + 0.35 * power_law + 0.6 * multiscale + 0.45 * ridge + 0.25 * coupling + noise + chaotic_mod