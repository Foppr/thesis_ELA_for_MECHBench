import numpy as np

class ChaoticSaddlePenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave components with dynamic amplitude modulation
        sine_wave = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + 0.5 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[i])
            freq_mod = 1.0 + 0.3 * np.sin(0.6 * x[i]) * np.cos(0.5 * x[i])
            sine_wave += amp_mod * np.sin(freq_mod * x[i] + 0.3 * np.sin(1.2 * x[i])) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive saddle-point conditioning with chaotic curvature
        saddle = 0.0
        for i in range(self.dim):
            curvature = 1.0 + 0.7 * np.sin(0.5 * x[i]) * np.cos(0.4 * x[i])
            saddle += curvature * (x[i]**2 - 0.3 * np.sin(0.8 * x[i])**2)
        
        # Dynamic penalty regions with chaotic boundary modulation
        penalty = 0.0
        for i in range(self.dim):
            boundary_mod = 1.0 + 0.4 * np.sin(0.9 * x[i]) * np.cos(0.3 * x[i])
            if np.abs(x[i]) > 2.0:
                penalty += boundary_mod * (x[i]**2 + 0.5 * np.sin(1.5 * x[i])**2)
            else:
                penalty += 0.1 * x[i]**4
        
        # Enhanced cross-dimensional coupling with chaotic phase interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(1.5 * (x[i] + x[j]) + 0.4 * np.cos(x[i] - x[j]))
                dist = np.sqrt((x[i] - x[j])**2 + 0.2)
                coupling += phase * np.exp(-0.4 * dist**2) * (x[i]**2 + x[j]**2 + 0.3 * x[i] * x[j])
        
        # Multi-scale penalty basin with piecewise curvature and chaotic transitions
        basin = 0.0
        for i in range(self.dim):
            if x[i] < -2.0:
                basin += 0.9 * np.sin(1.8 * x[i]) * np.exp(-0.2 * x[i]**2) + 0.3 * x[i]**4
            elif x[i] > 2.0:
                basin += 0.7 * np.cos(1.6 * x[i]) * np.exp(-0.15 * x[i]**2) + 0.2 * x[i]**3
            else:
                basin += 0.4 * x[i]**2 * np.exp(-0.25 * x[i]**2)
        
        # Chaotic harmonic interference with adaptive weights and penalty modulation (modified)
        harmonic = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.3 * np.sin(0.7 * x[i]) * np.cos(0.6 * x[i])
            # Modified: Changed frequency and added phase shift
            harmonic += weight * np.sin(2.5 * x[i] + 0.4 * np.sin(x[i] + 0.5)) * np.exp(-0.3 * np.abs(x[i]))
        
        # Combined fitness with variable weighting scheme and chaotic scaling (modified)
        total = 0.15 * sine_wave + 0.2 * saddle + 0.25 * penalty + 0.15 * coupling + 0.15 * basin + 0.1 * harmonic
        
        return total