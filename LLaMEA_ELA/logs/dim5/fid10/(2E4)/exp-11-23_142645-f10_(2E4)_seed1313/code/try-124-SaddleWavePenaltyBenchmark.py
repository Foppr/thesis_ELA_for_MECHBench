import numpy as np

class SaddleWavePenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave components with stochastic modulation
        wave_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.2 * np.sin(0.5 * x[i]) * np.cos(0.4 * x[i]) + 0.3 * np.random.rand()
            wave_term += freq * np.sin(freq * x[i] + 0.2 * np.sin(3.0 * x[i])) * np.exp(-0.2 * x[i]**2)
        
        # Adaptive saddle-point conditioning with variable curvature and stochastic perturbations
        saddle_condition = 0.0
        for i in range(self.dim):
            curvature = 1.5 + 0.5 * np.sin(0.6 * x[i]) * np.cos(0.8 * x[i]) + 0.2 * np.random.rand()
            saddle_condition += curvature * x[i]**2 * np.exp(-0.15 * np.abs(x[i])) + 0.1 * np.random.randn()
        
        # Dynamic penalty regions with stochastic zones and overlapping penalties
        penalty = 0.0
        for i in range(self.dim):
            # Stochastic penalty zones with varying intensities and positions
            if np.abs(x[i] - 2.5) < 0.3 or np.abs(x[i] + 2.5) < 0.3:
                penalty += 15.0 * np.exp(-0.5 * (x[i] - 2.5)**2) + 15.0 * np.exp(-0.5 * (x[i] + 2.5)**2)
            elif np.abs(x[i]) < 0.15:
                penalty += 8.0 * np.exp(-0.3 * x[i]**2)
            elif np.abs(x[i] - 1.0) < 0.25 or np.abs(x[i] + 1.0) < 0.25:
                penalty += 10.0 * np.exp(-0.4 * (x[i] - 1.0)**2) + 10.0 * np.exp(-0.4 * (x[i] + 1.0)**2)
            # Add stochastic perturbations to penalty
            penalty += 2.0 * np.random.rand()
        
        # Cross-term coupling with chaotic phase modulation and stochastic interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_mod = np.sin(4.0 * (x[i] + x[j]) + np.cos(2.5 * x[i] - x[j]) + 0.5 * np.random.rand())
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_coupling += phase_mod * np.exp(-0.2 * dist**2) * (x[i]**2 + x[j]**2) + 0.1 * np.random.randn()
        
        # Asymmetric oscillatory basin with stochastic transitions and noise
        asym_basin = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                asym_basin += 0.8 * np.sin(2.0 * x[i]) * np.exp(-0.15 * x[i]**2) + 0.3 * x[i]**3 + 0.05 * np.random.randn()
            else:
                asym_basin += 0.7 * np.cos(1.6 * x[i]) * np.exp(-0.1 * x[i]**2) + 0.2 * x[i]**4 + 0.05 * np.random.randn()
        
        # Multi-scale harmonic interference with stochastic amplitude and frequency modulation
        harmonic = 0.0
        for i in range(self.dim):
            amp_mod = 1.5 + 0.6 * np.cos(0.7 * x[i]) * np.sin(0.9 * x[i]) + 0.2 * np.random.rand()
            freq_mod = 3.0 + 1.0 * np.sin(0.8 * x[i]) * np.cos(0.6 * x[i]) + 0.1 * np.random.rand()
            harmonic += amp_mod * np.sin(freq_mod * x[i] + 0.7 * np.sin(x[i])) * np.exp(-0.35 * np.abs(x[i]))
        
        # Additional complexity with stochastic interaction terms
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  
                interaction += (x[i] * x[j]) / (1.0 + np.abs(x[i] - x[j])) * (1.0 + 0.2 * np.random.rand())
        
        # Combined fitness with randomized weights
        total = 0.22 * wave_term + 0.27 * saddle_condition + 0.20 * penalty + 0.23 * cross_coupling + 0.10 * asym_basin + 0.07 * harmonic + 0.06 * interaction
        
        return total