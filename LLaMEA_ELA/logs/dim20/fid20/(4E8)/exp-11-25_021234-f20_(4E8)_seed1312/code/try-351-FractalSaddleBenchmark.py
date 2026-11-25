import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal Brownian motion parameters
        self.hurst = 0.3
        self.fractal_scale = 1.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Brownian motion component
        fbm_term = 0.0
        for i in range(self.dim):
            # Compute fractal Brownian motion value with Hurst parameter
            fbm_val = self._fractal_brownian_motion(x[i], self.hurst)
            fbm_term += fbm_val * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            
        # Adaptive elliptic conditioning
        elliptic_term = 0.0
        for i in range(self.dim):
            # Dynamic elliptic parameters based on position
            a = 1.0 + 0.5 * np.sin(0.4 * i + 0.2 * np.sum(x**2))
            b = 1.0 + 0.3 * np.cos(0.3 * i + 0.1 * np.sum(x**2))
            c = 0.5 + 0.2 * np.sin(0.6 * i + 0.3 * np.sum(x**2))
            elliptic_term += a * x[i]**2 + b * x[i]**4 + c * x[i]**6
            
        # Gradient-based saddle-point interactions
        saddle_term = 0.0
        for i in range(self.dim):
            grad_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    diff = x[i] - x[j]
                    grad_sum += diff / (1.0 + diff**2)
            saddle_term += grad_sum * np.sin(0.7 * x[i])
            
        # Multi-scale harmonic modulation
        harmonic_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * i + 0.2 * np.sum(x**2))
            amp = 1.0 + 0.8 * np.cos(0.4 * i + 0.3 * np.sum(x**2))
            harmonic_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + 0.5)
            
        # Boundary repulsion with fractal scaling
        boundary_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist_from_boundary = 5.0 - np.abs(x[i])
                penalty = 2.0 * dist_from_boundary**2.5
                boundary_term += penalty * np.exp(-0.1 * x[i]**2)
                
        # Cross-dimensional coupling with adaptive weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 + 0.5 * np.sin(0.2 * (i + j) + 0.3 * np.sum(x**2))
                coupling_term += weight * (x[i]**2 + x[j]**2) * np.cos(x[i] - x[j])
                
        # Global conditioning with time-varying parameters
        r = np.sqrt(np.sum(x**2))
        global_factor = 1.0 + 0.3 * np.sin(0.5 * r)
        
        # Combine all terms
        total = fbm_term + elliptic_term + saddle_term + harmonic_term + boundary_term + coupling_term
        return total * global_factor
        
    def _fractal_brownian_motion(self, x, hurst):
        """Simple approximation of fractal Brownian motion"""
        # This is a simplified version for the benchmark
        return np.sin(x) * np.cos(0.5 * x) * np.exp(-0.1 * np.abs(x)) * (1.0 + 0.2 * np.sin(2.0 * x))