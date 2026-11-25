import numpy as np

class PeriodicHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic frequencies and coupling strengths
        self.frequencies = [2.0 + 1.5 * np.sin(i * 0.5) for i in range(dim)]
        self.coupling_strengths = [0.8 + 0.3 * np.cos(i * 0.3) for i in range(dim)]
        self.conditioning_factors = [1.0 + 0.5 * np.sin(i * 0.7) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic oscillatory component with varying frequencies
        oscillatory_term = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i % len(self.frequencies)]
            oscillatory_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Exponential conditioning term with position-dependent scaling
        exp_conditioning = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning_factors[i % len(self.conditioning_factors)]
            exp_conditioning += cond_factor * np.exp(0.1 * x[i]**2) * np.sin(2 * x[i])
            
        # Coupled harmonic potentials with extended interactions
        harmonic_term = 0.0
        for i in range(self.dim):
            coupling = self.coupling_strengths[i % len(self.coupling_strengths)]
            # Self harmonic potential
            harmonic_term += 0.5 * x[i]**2
            # Coupled terms with neighbors
            for j in range(i+1, min(i+4, self.dim)):
                coupling_factor = coupling * (1 + 0.3 * np.sin(0.5 * (x[i] + x[j])))
                harmonic_term += coupling_factor * np.cos(x[i] - x[j])
                
        # Multi-scale periodicity with nested structures
        nested_periodic = 0.0
        for i in range(self.dim):
            # Multiple periodic components with different periods
            periods = [1.0, 2.0, 3.0, 4.0]
            for period in periods:
                nested_periodic += np.sin(period * x[i]) * np.cos(period * x[i])
                
        # Asymmetric exponential potentials to create complex basins
        asym_exp = 0.0
        for i in range(self.dim):
            # Asymmetric exponential terms
            asym_exp += np.exp(0.2 * x[i]**2) * (1 + 0.3 * np.sin(0.8 * x[i]))
            
        # Combine all terms with adaptive weights
        weights = [0.25, 0.20, 0.25, 0.20, 0.10]
        total = (weights[0] * oscillatory_term + 
                weights[1] * exp_conditioning + 
                weights[2] * harmonic_term + 
                weights[3] * nested_periodic + 
                weights[4] * asym_exp)
                
        # Global scaling factor with dimensionality dependence
        scale = 1.0 + 0.3 * np.log(self.dim + 1) + 0.05 * np.sum(np.abs(x))
        
        return scale * total