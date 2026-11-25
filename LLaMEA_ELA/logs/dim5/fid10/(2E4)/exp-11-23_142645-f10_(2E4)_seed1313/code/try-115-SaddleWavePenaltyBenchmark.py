import numpy as np

class SaddleWavePenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave interference with logistic map modulation
        wave_term = 0.0
        for i in range(self.dim):
            # Logistic map for chaotic frequency modulation
            freq = 3.8 * np.sin(0.5 * x[i]) * (1 - np.sin(0.5 * x[i])**2)
            wave_term += freq * np.sin(freq * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Adaptive elliptic conditioning with dynamic eccentricity
        elliptic_condition = 0.0
        for i in range(self.dim):
            # Dynamic eccentricity based on position and dimension
            eccentricity = 1.0 + 0.4 * np.sin(0.3 * x[i]) * np.cos(0.7 * x[i])
            elliptic_condition += eccentricity * x[i]**2 * np.exp(-0.05 * np.abs(x[i]))
        
        # Dynamic gradient-based penalty regions with directional sensitivity
        penalty = 0.0
        for i in range(self.dim):
            # Create penalty zones with gradient-sensitive decay
            if np.abs(x[i] - 1.5) < 0.4 or np.abs(x[i] + 1.5) < 0.4:
                penalty += 12.0 * np.exp(-0.3 * (x[i] - 1.5)**2) + 12.0 * np.exp(-0.3 * (x[i] + 1.5)**2)
            elif np.abs(x[i]) < 0.2:
                penalty += 6.0 * np.exp(-0.4 * x[i]**2)
        
        # Cross-term coupling with chaotic phase modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic phase modulation using sine and cosine combinations
                phase_mod = np.sin(3.0 * (x[i] + x[j]) + np.cos(x[i] - x[j]) * np.sin(x[i] + x[j]))
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_coupling += phase_mod * np.exp(-0.15 * dist**2) * (x[i]**2 + x[j]**2)
        
        # Asymmetric gradient basin with piecewise chaotic transitions
        asym_basin = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                asym_basin += 0.6 * np.sin(1.8 * x[i]) * np.exp(-0.12 * x[i]**2) + 0.25 * x[i]**3
            else:
                asym_basin += 0.5 * np.cos(1.4 * x[i]) * np.exp(-0.08 * x[i]**2) + 0.15 * x[i]**4
        
        # Multi-scale chaotic harmonic interference with dynamic amplitude modulation
        harmonic = 0.0
        for i in range(self.dim):
            # Chaotic amplitude modulation using sine and cosine combinations
            amp_mod = 1.0 + 0.4 * np.sin(0.6 * x[i]) * np.cos(0.8 * x[i])
            harmonic += amp_mod * np.sin(2.5 * x[i] + 0.6 * np.sin(x[i])) * np.exp(-0.3 * np.abs(x[i]))
        
        # Combined fitness with weighted components
        total = 0.3 * wave_term + 0.25 * elliptic_condition + 0.18 * penalty + 0.22 * cross_coupling + 0.12 * asym_basin + 0.15 * harmonic
        
        return total