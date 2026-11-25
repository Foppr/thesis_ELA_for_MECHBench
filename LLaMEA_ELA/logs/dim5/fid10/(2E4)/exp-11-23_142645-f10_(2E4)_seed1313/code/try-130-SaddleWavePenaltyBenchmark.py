import numpy as np

class SaddleWavePenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced periodic cosine wave components with frequency modulation
        wave_term = 0.0
        for i in range(self.dim):
            freq = 1.9 + 0.5 * np.sin(0.6 * x[i]) * np.cos(0.3 * x[i])
            wave_term += freq * np.cos(freq * x[i]) * np.exp(-0.25 * x[i]**2)
        
        # Enhanced adaptive saddle-point conditioning with variable curvature
        saddle_condition = 0.0
        for i in range(self.dim):
            # Variable curvature based on position and dimension
            curvature = 1.4 + 0.2 * np.sin(0.7 * x[i]) * np.cos(0.9 * x[i])
            saddle_condition += curvature * x[i]**2 * np.exp(-0.18 * np.abs(x[i]))
        
        # Enhanced dynamic penalty regions with multiple zones
        penalty = 0.0
        for i in range(self.dim):
            # Multiple penalty zones with varying intensities and shifted positions
            if np.abs(x[i] - 1.8) < 0.3 or np.abs(x[i] + 1.8) < 0.3:
                penalty += 16.0 * np.exp(-0.5 * (x[i] - 1.8)**2) + 16.0 * np.exp(-0.5 * (x[i] + 1.8)**2)
            elif np.abs(x[i]) < 0.1:
                penalty += 9.0 * np.exp(-0.35 * x[i]**2)
            elif np.abs(x[i] - 1.0) < 0.2 or np.abs(x[i] + 1.0) < 0.2:
                penalty += 11.0 * np.exp(-0.45 * (x[i] - 1.0)**2) + 11.0 * np.exp(-0.45 * (x[i] + 1.0)**2)
        
        # Enhanced cross-term coupling with complex phase modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_mod = np.sin(2.7 * (x[i] + x[j]) + np.cos(1.3 * x[i] - x[j]))
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_coupling += phase_mod * np.exp(-0.22 * dist**2) * (x[i]**2 + x[j]**2)
        
        # Enhanced asymmetric oscillatory basin with piecewise smooth transitions
        asym_basin = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                asym_basin += 0.75 * np.sin(2.1 * x[i]) * np.exp(-0.16 * x[i]**2) + 0.35 * x[i]**3
            else:
                asym_basin += 0.65 * np.cos(1.7 * x[i]) * np.exp(-0.11 * x[i]**2) + 0.25 * x[i]**4
        
        # Enhanced multi-scale harmonic interference with complex amplitude modulation
        harmonic = 0.0
        for i in range(self.dim):
            amp_mod = 1.4 + 0.25 * np.cos(0.8 * x[i]) * np.sin(0.8 * x[i])
            harmonic += amp_mod * np.sin(2.9 * x[i] + 0.6 * np.sin(x[i])) * np.exp(-0.37 * np.abs(x[i]))
        
        # Additional complexity with interaction terms (modified)
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Slightly increased interaction range
                interaction += (x[i] * x[j]) / (1.0 + 0.6 * np.abs(x[i] - x[j]))
        
        # Combined fitness with optimized weights
        total = 0.23 * wave_term + 0.24 * saddle_condition + 0.19 * penalty + 0.21 * cross_coupling + 0.09 * asym_basin + 0.07 * harmonic + 0.07 * interaction
        
        return total