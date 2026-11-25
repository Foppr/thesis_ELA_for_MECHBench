import numpy as np

class ChaoticSpiralSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logarithmic spiral components with dynamic radius modulation
        spiral = 0.0
        for i in range(self.dim):
            radius_mod = 1.0 + 0.5 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[i])
            angle_mod = 1.0 + 0.3 * np.sin(0.9 * x[i]) * np.cos(0.6 * x[i])
            spiral += radius_mod * np.exp(-0.1 * x[i]**2) * np.sin(angle_mod * np.log(np.abs(x[i]) + 1e-8) + 0.5 * np.cos(1.3 * x[i]))
        
        # Adaptive saddle-point coupling with chaotic curvature
        saddle = 0.0
        for i in range(self.dim):
            curvature = 1.0 + 0.4 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            saddle += curvature * (x[i]**2 - 0.5 * np.sin(2.0 * x[i])**2)
        
        # Dynamic curvature modulation with chaotic phase coupling
        curvature_mod = 0.0
        for i in range(self.dim):
            phase = 1.0 + 0.6 * np.sin(0.8 * x[i]) * np.cos(0.5 * x[i])
            curvature_mod += phase * (x[i]**4 + 0.3 * x[i]**3 + 0.2 * x[i]**2)
        
        # Cross-dimensional chaotic ridge coupling
        ridge = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(1.5 * (x[i] - x[j]) + 0.4 * np.cos(x[i] + x[j]))
                ridge += coupling * np.exp(-0.2 * (x[i]**2 + x[j]**2)) * (x[i]**2 + x[j]**2)
        
        # Multi-scale chaotic basin with piecewise exponential curvature
        basin = 0.0
        for i in range(self.dim):
            if x[i] < -2.0:
                basin += 0.7 * np.exp(-0.1 * (x[i] + 2.0)**2) * np.sin(3.0 * x[i])
            elif x[i] > 2.0:
                basin += 0.5 * np.exp(-0.1 * (x[i] - 2.0)**2) * np.cos(2.5 * x[i])
            else:
                basin += 0.3 * np.exp(-0.2 * x[i]**2) * (x[i]**3 + 0.5 * x[i])
        
        # Chaotic harmonic interference with variable amplitude
        harmonic = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i])
            harmonic += amp * np.exp(-0.15 * np.abs(x[i])) * np.sin(2.0 * x[i] + 0.3 * np.sin(x[i]))
        
        # Combined fitness with variable weighting scheme
        total = 0.2 * spiral + 0.25 * saddle + 0.2 * curvature_mod + 0.15 * ridge + 0.15 * basin + 0.05 * harmonic
        
        return total