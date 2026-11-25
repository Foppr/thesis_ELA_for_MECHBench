import numpy as np

class ChaoticEllipticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic oscillatory components with dynamic frequency modulation
        oscillation = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.3 * np.sin(0.8 * x[i]) * np.cos(0.6 * x[i])
            amp_mod = 1.0 + 0.4 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            oscillation += amp_mod * np.sin(freq_mod * x[i] + 0.2 * np.sin(1.5 * x[i])) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive elliptic conditioning with chaotic eccentricity
        elliptic = 0.0
        for i in range(self.dim):
            eccentricity = 1.0 + 0.6 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[i])
            elliptic += eccentricity * (x[i]**2 + 0.5 * np.sin(0.7 * x[i])**2)
        
        # Dynamic gradient modulation with chaotic amplitude
        gradient_mod = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.9 * x[i]) * np.cos(0.4 * x[i])
            gradient_mod += amp * np.exp(-0.2 * x[i]**2) * (x[i]**3 + 0.3 * x[i])
        
        # Cross-dimensional coupling with chaotic phase interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = np.sin(1.2 * (x[i] + x[j]) + 0.5 * np.cos(x[i] - x[j]))
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                coupling += phase * np.exp(-0.3 * dist**2) * (x[i]**2 + x[j]**2)
        
        # Multi-scale chaotic basin with piecewise curvature
        basin = 0.0
        for i in range(self.dim):
            if x[i] < -1.0:
                basin += 0.8 * np.sin(2.0 * x[i]) * np.exp(-0.15 * x[i]**2) + 0.2 * x[i]**4
            elif x[i] > 1.0:
                basin += 0.6 * np.cos(1.8 * x[i]) * np.exp(-0.2 * x[i]**2) + 0.3 * x[i]**3
            else:
                basin += 0.5 * x[i]**2 * np.exp(-0.3 * x[i]**2)
        
        # Chaotic harmonic interference with adaptive weights
        harmonic = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.4 * np.sin(0.6 * x[i]) * np.cos(0.5 * x[i])
            harmonic += weight * np.sin(2.5 * x[i] + 0.3 * np.sin(x[i])) * np.exp(-0.25 * np.abs(x[i]))
        
        # Combined fitness with variable weighting scheme
        total = 0.2 * oscillation + 0.25 * elliptic + 0.15 * gradient_mod + 0.2 * coupling + 0.15 * basin + 0.05 * harmonic
        
        return total