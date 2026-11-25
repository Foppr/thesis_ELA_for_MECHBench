import numpy as np

class SaddleWavePenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic cosine wave components with varying frequencies
        wave_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.6 * np.sin(0.4 * x[i])
            wave_term += freq * np.cos(freq * x[i]) * np.exp(-0.25 * x[i]**2)
        
        # Adaptive saddle-point conditioning with dynamic curvature
        saddle_condition = 0.0
        for i in range(self.dim):
            # Dynamic curvature based on position
            curvature = 1.0 + 0.4 * np.cos(0.5 * x[i]) * np.sin(0.7 * x[i])
            saddle_condition += curvature * x[i]**2 * np.exp(-0.15 * np.abs(x[i]))
        
        # Dynamic penalty regions with exponential decay
        penalty = 0.0
        for i in range(self.dim):
            # Create penalty zones around specific values
            if np.abs(x[i] - 2.0) < 0.4 or np.abs(x[i] + 2.0) < 0.4:
                penalty += 12.0 * np.exp(-0.6 * (x[i] - 2.0)**2) + 12.0 * np.exp(-0.6 * (x[i] + 2.0)**2)
            elif np.abs(x[i]) < 0.25:
                penalty += 6.0 * np.exp(-0.35 * x[i]**2)
        
        # Cross-term coupling with periodic phase modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_mod = np.sin(2.5 * (x[i] + x[j]) + np.cos(x[i] - x[j]))
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_coupling += phase_mod * np.exp(-0.15 * dist**2) * (x[i]**2 + x[j]**2)
        
        # Asymmetric oscillatory basin with piecewise smooth transitions
        asym_basin = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                asym_basin += 0.6 * np.sin(1.6 * x[i]) * np.exp(-0.12 * x[i]**2) + 0.25 * x[i]**3
            else:
                asym_basin += 0.5 * np.cos(1.3 * x[i]) * np.exp(-0.08 * x[i]**2) + 0.15 * x[i]**4
        
        # Multi-scale harmonic interference with dynamic amplitude modulation
        harmonic = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + 0.4 * np.cos(0.6 * x[i]) * np.sin(0.8 * x[i])
            harmonic += amp_mod * np.sin(2.5 * x[i] + 0.6 * np.sin(x[i])) * np.exp(-0.3 * np.abs(x[i]))
        
        # Combined fitness with weighted components
        total = 0.3 * wave_term + 0.25 * saddle_condition + 0.18 * penalty + 0.22 * cross_coupling + 0.12 * asym_basin + 0.13 * harmonic
        
        return total