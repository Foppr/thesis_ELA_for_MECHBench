import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine map with dynamic frequency modulation
        sine_map = 0.0
        for i in range(self.dim):
            freq = 1.8 + 0.4 * np.sin(i * 0.5 + np.pi/6)
            sine_map += np.sin(freq * x[i]) * (1.0 + 0.2 * np.cos(i * 0.3))
        
        # Modified Gaussian radial basis functions with phase-shifted centers
        rbf_sum = 0.0
        for i in range(min(5, self.dim)):
            center = 3.0 * np.sin(i * 0.7 + np.pi/4) + 2.0 * np.cos(i * 0.9)
            width = 0.8 + 0.2 * np.sin(i * 0.6)
            rbf_sum += np.exp(-0.5 * ((x[i] - center) / width)**2) * (1.0 + 0.15 * np.sin(i * 0.8))
        
        # Polynomial coupling with variable exponents and adaptive weights
        poly_coupling = 0.0
        for i in range(self.dim - 2):
            weight = 0.7 + 0.3 * np.cos(i * 0.4)
            exp1, exp2, exp3 = 2 + int(i % 3), 3 + int(i % 4), 2 + int((i+1) % 3)
            poly_coupling += weight * x[i]**exp1 * x[i+1]**exp2 * x[i+2]**exp3
        
        # Hyperbolic tangent coupling with dynamic scaling
        tanh_coupling = 0.0
        for i in range(self.dim - 1):
            scale = 0.5 + 0.3 * np.sin(i * 0.6)
            tanh_coupling += scale * np.tanh(0.5 * x[i]) * np.tanh(0.3 * x[i+1])
        
        # Novel cross-dimensional interaction with cosine modulation
        cross_term = 0.0
        for i in range(self.dim - 2):
            mod = 1.0 + 0.2 * np.cos(i * 0.5)
            cross_term += mod * (x[i] - x[i+1])**2 * np.cos(x[i] + x[i+1])
        
        # Adaptive noise with frequency-dependent amplitude
        noise_amp = 0.04 * (1.0 + 0.3 * np.sin(self.dim * 0.4))
        noise = noise_amp * np.sum(np.sin(3.0 * x) * np.cos(1.5 * x)) * np.random.rand()
        
        # Dynamic conditioning with multi-scale factors and entropy-based scaling
        entropy = -np.mean(np.abs(x) * np.log(np.abs(x) + 1e-10))
        condition_factor = 1.0 + 0.2 * np.sin(self.dim * 0.3) * np.mean(np.abs(x)) + \
                          0.15 * np.cos(self.dim * 0.5) * entropy + \
                          0.1 * np.sin(self.dim * 0.7) * np.std(x)**2
        
        # Quadratic base with enhanced coupling and dynamic scaling
        quadratic = condition_factor * (np.sum(x**2) + 0.2 * np.sum(x**4) + 0.08 * np.sum(np.abs(x)**3))
        
        # Novel hyperbolic sine coupling term with directional weighting
        sinh_coupling = 0.5 * np.sum(np.sinh(0.3 * x[:-2]) * np.cosh(0.15 * x[2:]) * np.cos(0.2 * x[:-2]))
        
        # Final combined function value
        return quadratic + sine_map + rbf_sum + poly_coupling + tanh_coupling + sinh_coupling + cross_term + noise