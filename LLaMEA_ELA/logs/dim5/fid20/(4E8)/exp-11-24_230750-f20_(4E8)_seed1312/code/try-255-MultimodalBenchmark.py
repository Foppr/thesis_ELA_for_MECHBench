import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic tangent skewness component
        tanh_skew = 0.0
        for i in range(self.dim):
            tanh_skew += np.tanh(x[i] * (1 + 0.1 * np.sin(i))) * np.exp(-0.1 * x[i]**2)
        
        # Multi-modal sine-wave interaction terms
        sine_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sine_interaction += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2))
        
        # Adaptive elliptic valley component with varying eccentricity
        elliptic_valley = 0.0
        for i in range(self.dim):
            eccentricity = 1 + 0.5 * np.sin(0.3 * i)
            elliptic_valley += (x[i]**2) / (1 + eccentricity * np.cos(0.2 * x[i]))
        
        # Chaotic logistic map inspired gradient deception
        logistic_deception = 0.0
        r = 3.8 + 0.2 * np.sin(0.5 * self.dim)
        for i in range(self.dim):
            if i == 0:
                val = x[i]
            else:
                val = x[i-1]
            logistic_deception += (val * r * (1 - val))**2
        
        # Multi-scale Gaussian interference with dynamic phase shifts
        gaussian_interference = 0.0
        phases = [0, np.pi/4, np.pi/2, 3*np.pi/4]
        for phase in phases:
            for i in range(self.dim):
                gaussian_interference += np.exp(-0.5 * ((x[i] - np.sin(phase)) / (0.5 + 0.5 * np.cos(phase)))**2)
        
        # Cross-dimensional coupling with adaptive weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.5 * np.sin(0.1 * (i + j))
                cross_coupling += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Combined fitness function
        return 0.25 * tanh_skew + 0.20 * sine_interaction + 0.20 * elliptic_valley + 0.15 * logistic_deception + 0.10 * gaussian_interference + 0.10 * cross_coupling