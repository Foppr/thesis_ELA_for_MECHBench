import numpy as np

class SaddleWavePenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave components with varying frequencies and chaos modulation
        wave_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.8 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            wave_term += freq * np.sin(freq * x[i] + 0.2 * np.sin(2.0 * x[i])) * np.exp(-0.3 * x[i]**2)
        
        # Adaptive saddle-point conditioning with chaotic curvature
        saddle_condition = 0.0
        for i in range(self.dim):
            # Chaotic curvature based on position
            curvature = 1.0 + 0.5 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i])
            saddle_condition += curvature * x[i]**2 * np.exp(-0.2 * np.abs(x[i]))
        
        # Dynamic penalty regions with chaotic decay
        penalty = 0.0
        for i in range(self.dim):
            # Create chaotic penalty zones around specific values
            if np.abs(x[i] - 1.8) < 0.3 or np.abs(x[i] + 1.8) < 0.3:
                penalty += 15.0 * np.exp(-0.7 * (x[i] - 1.8)**2) + 15.0 * np.exp(-0.7 * (x[i] + 1.8)**2)
            elif np.abs(x[i]) < 0.15:
                penalty += 8.0 * np.exp(-0.5 * x[i]**2)
        
        # Enhanced cross-term coupling with chaotic phase modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_mod = np.sin(2.0 * (x[i] + x[j]) + np.cos(x[i] - x[j]) * np.sin(0.5 * (x[i] + x[j])))
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_coupling += phase_mod * np.exp(-0.2 * dist**2) * (x[i]**2 + x[j]**2)
        
        # Chaotic asymmetric oscillatory basin with piecewise smooth transitions
        asym_basin = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                asym_basin += 0.7 * np.sin(1.5 * x[i]) * np.exp(-0.2 * x[i]**2) + 0.3 * x[i]**3
            else:
                asym_basin += 0.4 * np.cos(1.6 * x[i]) * np.exp(-0.1 * x[i]**2) + 0.2 * x[i]**4
        
        # Multi-scale chaotic harmonic interference with dynamic amplitude modulation
        harmonic = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + 0.5 * np.sin(0.7 * x[i]) * np.cos(0.5 * x[i])
            harmonic += amp_mod * np.sin(3.0 * x[i] + 0.7 * np.sin(x[i]) * np.cos(0.5 * x[i])) * np.exp(-0.35 * np.abs(x[i]))
        
        # Combined fitness with weighted components
        total = 0.25 * wave_term + 0.2 * saddle_condition + 0.2 * penalty + 0.15 * cross_coupling + 0.15 * asym_basin + 0.05 * harmonic
        
        return total