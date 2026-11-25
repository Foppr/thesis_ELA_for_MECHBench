import numpy as np

class HyperchaoticTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize hyperchaotic parameters with exponential decay modulation
        self.freqs = np.array([1.5 * np.exp(-0.1 * i) + 0.5 * np.sin(0.3 * np.pi * i) for i in range(dim)])
        self.amps = np.array([2.0 * np.exp(-0.05 * i) + 0.8 * np.cos(0.4 * np.pi * i) for i in range(dim)])
        self.phases = np.array([0.2 * np.sin(0.6 * np.pi * i) + 0.1 * np.cos(0.7 * np.pi * i) for i in range(dim)])
        # Dynamic conditioning weights with sinusoidal modulation
        self.cond_weights = np.array([1.0 + 0.3 * np.sin(0.5 * np.pi * i + 0.2 * np.sum(np.arange(dim))) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay trigonometric component with complex coupling
        exp_trig_component = 0.0
        for i in range(self.dim):
            inner_sum = np.sum([self.freqs[j] * np.sin(self.amps[j] * x[j] + self.phases[j]) for j in range(self.dim)])
            exp_trig_component += np.exp(-0.5 * (x[i] - inner_sum)**2) * np.cos(self.freqs[i] * x[i] + self.phases[i])
        exp_trig_component /= self.dim
        
        # Multi-scale chaotic interaction with dynamic phase shifts
        chaotic_interaction = 0.0
        for i in range(self.dim):
            phase_shift = np.sin(0.8 * np.pi * i + 0.3 * np.sum(x)) * np.cos(0.4 * np.pi * i)
            chaotic_interaction += np.sin(self.freqs[i] * x[i] + phase_shift) * np.exp(-0.2 * x[i]**2)
        chaotic_interaction /= self.dim
        
        # Adaptive conditioning with exponential weights
        adaptive_cond = 0.0
        for i in range(self.dim):
            weight = self.cond_weights[i] * np.exp(-0.1 * np.abs(x[i]))
            adaptive_cond += weight * x[i]**3 * np.sin(0.5 * np.pi * x[i])
        adaptive_cond /= self.dim
        
        # Cross-dimensional hyperchaotic coupling with exponential interaction
        cross_hyperspace = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = np.exp(-0.3 * (x[i]**2 + x[j]**2)) * np.sin(0.6 * np.pi * (i - j))
                cross_hyperspace += coupling_strength * np.exp(-0.1 * np.abs(x[i] - x[j]))
        cross_hyperspace /= (self.dim * (self.dim - 1) / 2.0)
        
        # Final combination with dynamic scaling
        result = 0.4 * exp_trig_component + 0.3 * chaotic_interaction + 0.2 * adaptive_cond + 0.1 * cross_hyperspace
        
        return result