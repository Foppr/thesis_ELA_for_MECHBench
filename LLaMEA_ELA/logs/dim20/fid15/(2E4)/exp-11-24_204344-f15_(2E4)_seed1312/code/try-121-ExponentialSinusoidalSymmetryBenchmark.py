import numpy as np

class ExponentialSinusoidalSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Fractal-like radial component with self-similar chaotic patterns and memory effects
        r = np.sqrt(np.sum(x**2))
        radial = (np.exp(-0.1 * r) * (np.sin(15 * r + np.sin(5 * r)) + 0.4 * np.cos(8 * r)) + 
                  0.2 * np.sin(4 * r) * np.cos(2 * r) + 0.1 * np.sin(r**1.5))
        
        # Irregular sinusoidal modulations with fractional frequency shifts and amplitude variations
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i * 0.7) + 1.0 * np.cos(i * 1.3)
            amp = 0.9 + 0.5 * np.sin(i * 0.9) + 0.3 * np.cos(i * 1.1)
            phase = 1.0 + 0.4 * np.sin(i * 1.0)
            sin_mod += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase * 0.7)
        
        # Complex exponential decay with fractional scaling and multiple peaks
        exp_decay = 0.0
        for i in range(self.dim):
            scale = 1.5 / (1.0 + np.exp(-x[i] + 1.0)) + 0.4 * np.sin(x[i] * 2.5) + 0.2 * np.cos(x[i] * 1.8)
            exp_decay += scale * np.exp(-0.5 * (x[i] - 1.0)**2) * np.sin(7.0 * x[i] + np.cos(x[i]))
        
        # Cross-dimensional chaotic interaction with fractional coupling and asymmetric interactions
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.25 * (x[i]**2 + x[j]**2)) * np.cos(5.0 * x[i] * x[j] + np.sin(x[i] + x[j]))
                cross_exp += coupling * (1.0 + 0.4 * np.sin(i * j * 0.7) + 0.3 * np.cos(i * j * 0.5))
        
        # Multi-scale harmonic landscape with fractal-like amplitudes and frequencies
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.5 + 1.2 * np.sin(i * 0.6) + 0.6 * np.cos(i * 0.8)
            amp = 1.5 + 0.4 * np.sin(i * 0.7) + 0.2 * np.cos(i * 0.9)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + np.sin(x[i]))
        
        # Oscillatory behavior with fractional decay and irregular frequencies
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 20 + 8 * np.sin(i * 0.5)
            oscillatory += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.15 * np.abs(x[i])) * (1.0 + 0.3 * np.sin(x[i] * 5))
        
        # Asymmetric potential wells with fractal minima and irregular energy barriers
        wells = 0.0
        for i in range(self.dim):
            min_pos = 1.5 + 0.7 * np.sin(i * 0.8)
            well_depth = 1.5 + 0.5 * np.cos(i * 0.6)
            wells += (x[i]**2 - 2.5 * x[i] + min_pos) * np.exp(-0.3 * (x[i] - min_pos)**2) * well_depth
        
        # Memory-dependent dynamics with chaotic temporal weights
        memory = 0.0
        for i in range(self.dim):
            memory += 0.1 * np.sin(x[i]) * np.cos(x[i] * 0.5) * np.exp(-0.2 * x[i]**2)
        
        # Final combination with fractional weights and additional complexity
        return (0.6 * radial + 0.7 * sin_mod + 0.8 * exp_decay + 0.9 * cross_exp + 
                1.0 * harmonic + 1.1 * oscillatory + 1.2 * wells + 0.3 * np.sum(np.abs(x)) + 0.15 * memory)