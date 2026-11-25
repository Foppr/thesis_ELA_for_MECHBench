import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired interference with complex sinusoidal modulation
        quantum_term = 0.0
        for i in range(self.dim):
            if i == 0:
                xi_prev = x[-1] if self.dim > 1 else 0
            else:
                xi_prev = x[i-1]
            quantum_term += np.sin(xi_prev * np.pi * (1 - xi_prev)) * np.cos(x[i] * np.pi) * np.exp(-0.1 * x[i]**2)
        quantum_term /= self.dim
        
        # Fractal-like self-similarity with multi-scale harmonic interactions
        fractal_term = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(0.5 * np.pi * i)
            fractal_term += scale_factor * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.2 * np.abs(x[i]))
        fractal_term /= self.dim
        
        # Enhanced cross-dimensional coupling with dynamic phase shifts
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = np.sin(0.3 * (i - j))
                cross_term += np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(x[i] + x[j] + phase_shift)
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-modal structure with asymmetric sine-wave basin modulation
        modal_term = np.sum(np.sin(3.0 * np.pi * x) * np.cos(0.7 * np.pi * x) * np.exp(-0.1 * x**2)) / self.dim
        
        # Dynamic noise injection with chaotic amplitude modulation
        noise_amp = 0.2 + 0.1 * np.sin(0.4 * np.sum(x))
        noise_term = np.sum(noise_amp * np.sin(x * np.pi * (1 + 0.1 * x))) / self.dim
        
        # Polynomial distortion with quantum-like coefficients
        poly_term = np.sum(0.6 * x**6 - 2.8 * x**5 + 3.9 * x**4 - 2.4 * x**3 + 0.8 * x**2) / self.dim
        
        # Asymmetric radial component with quantum harmonic interference
        radial_term = np.sum(np.sin(0.7 * np.pi * np.sqrt(np.sum(x**2))) * np.cos(0.3 * np.pi * np.sqrt(np.sum(x**2))) * np.exp(-0.15 * np.sum(x**2))) / self.dim
        
        # Add a new hyperbolic tangent interaction term for increased complexity
        tanh_term = 0.0
        for i in range(self.dim):
            tanh_term += np.tanh(2.0 * x[i]) * np.sin(0.5 * np.pi * x[i])
        tanh_term /= self.dim
        
        # Add a new asymmetric radial basis function with dynamic scaling
        rbf_term = 0.0
        for i in range(self.dim):
            rbf_term += np.exp(-0.5 * (x[i] - 1.0)**2) * np.sin(2.0 * np.pi * x[i]) * np.cos(0.3 * np.pi * x[i])
        rbf_term /= self.dim
        
        # Introduce a new fractional Brownian motion inspired term for increased complexity
        fbm_term = 0.0
        for i in range(self.dim):
            fbm_term += np.sin(np.pi * x[i] * (1 + 0.3 * np.cos(0.2 * np.pi * i))) * np.exp(-0.1 * x[i]**2)
        fbm_term /= self.dim
        
        # Introduce a new chaotic logistic map based interaction term
        logistic_term = 0.0
        for i in range(self.dim):
            r = 3.9  # Chaos parameter
            if i == 0:
                xi_prev = x[-1] if self.dim > 1 else 0
            else:
                xi_prev = x[i-1]
            logistic_term += np.sin(r * xi_prev * (1 - xi_prev)) * np.cos(x[i])
        logistic_term /= self.dim
        
        # Combine all terms with optimized weights
        total = 0.15 * quantum_term + 0.14 * fractal_term + 0.13 * cross_term + 0.12 * modal_term + 0.11 * noise_term + 0.10 * poly_term + 0.09 * radial_term + 0.08 * tanh_term + 0.07 * rbf_term + 0.05 * fbm_term + 0.06 * logistic_term
        
        return total