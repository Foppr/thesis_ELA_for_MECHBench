import numpy as np

class PeriodicMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal periodic components with varying frequencies and amplitudes
        periodic = 0.0
        for i in range(self.dim):
            freq = 1.5 + 4.0 * np.sin(0.8 * i)
            amp = 0.8 + 0.7 * np.cos(0.6 * i)
            periodic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8)
        
        # Enhanced exponential decay interactions with modified coupling
        decay_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                coupling = 0.4 + 0.6 * np.sin(0.4 * (i + j))
                decay_interaction += coupling * np.exp(-dist * 0.5) * np.sin(dist * 1.8)
        
        # Adaptive conditioning with higher-order terms and dynamic scaling
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 2.0 + 0.6 * np.sin(0.7 * i + 1.5)
            conditioning += cond_factor * (x[i]**4 + 0.4 * x[i]**6)
        
        # Multi-scale harmonic potentials with dynamic phase shifts and additional terms
        harmonic = 0.0
        for i in range(self.dim):
            phase_shift = 0.3 * np.sin(0.7 * i + 1.2)
            harmonic += (x[i]**2) * np.cos(x[i] + phase_shift) * np.exp(-0.3 * x[i]**2) + 0.15 * np.sin(4 * x[i])
        
        # Additional higher-order polynomial terms for increased complexity
        poly_terms = 0.0
        for i in range(self.dim):
            poly_terms += 0.3 * x[i]**5 + 0.2 * x[i]**7
        
        # Combined result with dynamic weighting and dimension-dependent scaling
        result = 0.25 * periodic + 0.4 * decay_interaction + 0.15 * conditioning + 0.15 * harmonic + 0.05 * poly_terms
        
        # Enhanced global scaling factor with non-linear dimension dependency
        scaling = 1.0 + 0.3 * np.log(self.dim + 1) + 0.08 * np.sin(0.4 * self.dim)
        
        return result * scaling