import numpy as np

class ChaoticLogisticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map parameters
        self.r = 3.95
        self.logistic_scale = 1.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map component
        logistic_term = 0.0
        for i in range(self.dim):
            # Compute chaotic logistic map value
            logistic_val = self._logistic_map(x[i], self.r)
            logistic_term += logistic_val * np.sin(0.7 * x[i]) * np.cos(0.4 * x[i])
            
        # Adaptive elliptic conditioning
        elliptic_term = 0.0
        for i in range(self.dim):
            # Dynamic elliptic parameters based on position
            a = 1.0 + 0.6 * np.sin(0.5 * i + 0.3 * np.sum(x**2))
            b = 1.0 + 0.4 * np.cos(0.4 * i + 0.2 * np.sum(x**2))
            c = 0.6 + 0.3 * np.sin(0.7 * i + 0.4 * np.sum(x**2))
            elliptic_term += a * x[i]**2 + b * x[i]**4 + c * x[i]**6
            
        # Gradient-based saddle-point interactions
        saddle_term = 0.0
        for i in range(self.dim):
            grad_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    diff = x[i] - x[j]
                    grad_sum += diff / (1.0 + np.abs(diff))
            saddle_term += grad_sum * np.cos(0.8 * x[i])
            
        # Multi-scale harmonic modulation
        harmonic_term = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.4 * i + 0.3 * np.sum(x**2))
            amp = 1.5 + 1.0 * np.cos(0.5 * i + 0.4 * np.sum(x**2))
            harmonic_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + 0.6)
            
        # Boundary repulsion with chaotic scaling
        boundary_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist_from_boundary = 5.0 - np.abs(x[i])
                penalty = 3.0 * dist_from_boundary**3.0
                boundary_term += penalty * np.exp(-0.15 * x[i]**2)
                
        # Cross-dimensional coupling with chaotic weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 + 0.6 * np.sin(0.3 * (i + j) + 0.4 * np.sum(x**2))
                coupling_term += weight * (x[i]**2 + x[j]**2) * np.sin(x[i] - x[j])
                
        # Global conditioning with chaotic parameters
        r = np.sqrt(np.sum(x**2))
        global_factor = 1.0 + 0.4 * np.sin(0.6 * r)
        
        # Combine all terms
        total = logistic_term + elliptic_term + saddle_term + harmonic_term + boundary_term + coupling_term
        return total * global_factor
        
    def _logistic_map(self, x, r):
        """Simple approximation of chaotic logistic map"""
        # This is a simplified version for the benchmark
        return np.sin(x) * np.cos(0.6 * x) * np.exp(-0.12 * np.abs(x)) * (1.0 + 0.3 * np.sin(2.5 * x))