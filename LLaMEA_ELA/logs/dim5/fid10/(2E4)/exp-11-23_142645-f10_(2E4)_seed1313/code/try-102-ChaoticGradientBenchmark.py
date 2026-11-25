import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave interactions with exponential modulation
        chaotic_term = 0.0
        for i in range(self.dim):
            term = x[i] ** 3
            for k in range(1, 8):
                # Chaotic modulation using logistic map-like behavior
                chaos_factor = np.sin(k * x[i] + np.sin(k * x[i])) * np.exp(-0.1 * np.abs(x[i]))
                term += 0.3 * np.sin(k * x[i]) * chaos_factor * (x[i] ** (2 + k % 4))
            chaotic_term += term
        
        # Adaptive elliptic conditioning with dynamic axis scaling
        elliptic_condition = 0.0
        for i in range(self.dim):
            # Dynamic scaling based on position
            scale = 1.0 + 0.4 * np.sin(0.5 * x[i]) * np.cos(0.7 * x[i])
            elliptic_condition += scale * (x[i] ** 2) * np.exp(-0.08 * x[i]**2)
        
        # Dynamic gradient reversal with position-dependent sign flips
        gradient_reversal = 0.0
        for i in range(self.dim):
            # Introduce sign changes based on position and frequency
            sign_flip = np.sign(np.sin(0.3 * x[i]) * np.cos(0.5 * x[i]))
            gradient_reversal += sign_flip * (x[i] ** 4) * np.exp(-0.15 * np.abs(x[i]))
        
        # Multi-scale oscillatory landscape with dynamic frequency adjustment
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.cos(0.4 * x[i])
            oscillatory += freq * np.sin(freq * x[i]) * np.exp(-0.3 * np.abs(x[i]))
        
        # Asymmetric basin with piecewise hyperbolic and polynomial components
        asymmetric_basin = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                asymmetric_basin += 0.6 * np.tanh(0.6 * x[i]) + 0.3 * x[i]**4
            else:
                asymmetric_basin += 0.4 * np.cosh(0.5 * x[i]) - 0.2 * x[i]**3
        
        # Cross-term coupling with chaotic phase interference
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                # Chaotic phase difference
                phase_diff = np.sin(3.0 * dist + np.sin(2.0 * dist)) * np.cos(1.5 * dist)
                weight = 1.0 + 0.5 * np.sin(x[i]) * np.cos(x[j]) * np.sin(0.8 * (x[i] + x[j]))
                cross_coupling += weight * phase_diff * (x[i]**2 + x[j]**2) * np.exp(-0.12 * dist**2)
        
        # Combined fitness value with dynamic weighting
        total = 0.3 * chaotic_term + 0.25 * elliptic_condition + 0.2 * gradient_reversal + 0.15 * oscillatory + 0.08 * asymmetric_basin + 0.02 * cross_coupling
        
        return total