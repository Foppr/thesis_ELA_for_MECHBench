import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperbolic tangent basin terms with quaternion-inspired symmetry breaking
        basin_term = 0.0
        for i in range(self.dim):
            steepness = 1.5 + 0.8 * np.sin(i * 1.2 + np.pi/4)
            # Add quaternion-like coupling between dimensions
            coupling = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    coupling += np.tanh(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
            basin_term += (np.tanh(steepness * x[i])**3 + 0.5 * coupling) * np.exp(-0.3 * x[i]**2)
        
        # Adaptive polynomial gradient flow with multi-scale exponents
        grad_term = 0.0
        for i in range(self.dim):
            # Multi-scale polynomial scaling with adaptive coefficients
            scale = 1.0 + 0.3 * np.sin(0.5 * i)
            grad_term += (scale * x[i]**2 + 0.4 * x[i]**5 + 0.2 * np.exp(0.3 * x[i]) + 
                         0.1 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])) * np.cos(0.4 * x[i])
        
        # Fractal-like logarithmic energy interactions with chaotic perturbations
        energy_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.001)
                # Add chaotic modulation to the interaction
                chaos_mod = np.sin(5.0 * dist) * np.cos(3.0 * dist)
                energy_term += (np.log(dist + 1.0) / (dist + 1.0)) * chaos_mod * (
                    np.sin(2.0 * x[i]) * np.cos(1.5 * x[j]) + 
                    0.2 * np.sin(4.0 * x[i]) * np.cos(2.5 * x[j])
                )
        
        # Enhanced chaotic saddle-point modulation with fractal-like perturbations
        chaotic_term = 0.0
        for i in range(self.dim):
            # Add multiple chaotic components with varying frequencies
            base_osc = np.sin(x[i]) * np.cos(x[i]) * np.exp(-0.1 * np.abs(x[i]))
            high_freq = np.sin(5.0 * x[i] + np.sin(3.0 * x[i])) * np.cos(4.0 * x[i])
            fractal_osc = np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.05 * x[i]**2)
            chaotic_term += base_osc + 0.5 * high_freq + 0.3 * fractal_osc
        
        # Global scaling with adaptive basin boundaries and exponential components
        global_term = 0.0
        for i in range(self.dim):
            # Add more complex global structure with varying exponents
            global_term += (0.6 * x[i]**4 * np.exp(-0.15 * x[i]**2) + 
                           0.3 * x[i] * np.sin(0.7 * x[i]) + 
                           0.2 * np.log(np.abs(x[i]) + 3.0) + 
                           0.1 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]))
        
        # Add a small chaotic noise component to increase landscape irregularity
        noise = 0.05 * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x))
        
        # Return the combined function value with enhanced regularization
        return basin_term + grad_term + energy_term + chaotic_term + global_term + noise + 0.01 * np.sum(x**2)