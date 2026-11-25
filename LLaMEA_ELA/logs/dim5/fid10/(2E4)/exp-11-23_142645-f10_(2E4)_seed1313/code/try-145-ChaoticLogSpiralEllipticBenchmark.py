import numpy as np

class ChaoticLogSpiralEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logarithmic spiral components with varying radii and angular frequencies
        spiral_term = 0.0
        for i in range(self.dim):
            radius = 1.0 + 0.7 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[i])
            angle_freq = 2.0 + 0.6 * np.sin(0.5 * x[i]) * np.cos(0.2 * x[i])
            spiral_term += radius * np.exp(-0.1 * x[i]**2) * np.sin(angle_freq * np.log(np.abs(x[i]) + 1.0))
        
        # Adaptive elliptic conditioning with chaotic eccentricity
        elliptic_condition = 0.0
        for i in range(self.dim):
            # Chaotic eccentricity based on position
            eccentricity = 0.5 + 0.5 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[i])
            elliptic_condition += (x[i]**2 / (1.0 + eccentricity * np.abs(x[i]))) * np.exp(-0.3 * x[i]**2)
        
        # Dynamic gradient modulation with chaotic amplitude
        grad_mod = 0.0
        for i in range(self.dim):
            # Chaotic amplitude modulation
            amp_mod = 1.0 + 0.4 * np.sin(0.6 * x[i]) * np.cos(0.3 * x[i])
            grad_mod += amp_mod * np.exp(-0.2 * x[i]**2) * np.cos(1.5 * x[i] + 0.3 * np.sin(x[i]))
        
        # Enhanced cross-term coupling with chaotic phase coupling
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_coupling = np.cos(1.2 * (x[i] + x[j]) + 0.5 * np.sin(x[i] - x[j]))
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_coupling += phase_coupling * np.exp(-0.3 * dist**2) * (x[i]**2 + x[j]**2)
        
        # Chaotic asymmetric basin with piecewise smooth transitions
        asym_basin = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                asym_basin += 0.6 * np.log(np.abs(x[i]) + 1.0) * np.exp(-0.25 * x[i]**2) + 0.4 * x[i]**3
            else:
                asym_basin += 0.5 * np.exp(x[i]) * np.exp(-0.15 * x[i]**2) + 0.3 * x[i]**4
        
        # Multi-scale chaotic harmonic interference with dynamic frequency modulation
        harmonic = 0.0
        for i in range(self.dim):
            freq_mod = 2.0 + 0.8 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            harmonic += np.exp(-0.2 * x[i]**2) * np.sin(freq_mod * x[i] + 0.4 * np.sin(0.7 * x[i]))
        
        # Combined fitness with weighted components
        total = 0.25 * spiral_term + 0.2 * elliptic_condition + 0.2 * grad_mod + 0.15 * cross_coupling + 0.15 * asym_basin + 0.05 * harmonic
        
        return total