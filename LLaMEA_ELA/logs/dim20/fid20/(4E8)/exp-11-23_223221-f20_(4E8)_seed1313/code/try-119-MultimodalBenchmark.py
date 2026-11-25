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
            steepness = 2.0 + 1.2 * np.sin(i * 1.5 + np.pi/3)
            # Add quaternion-like coupling between dimensions with chaotic modulation
            coupling = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    coupling += np.tanh(x[i] * x[j]) * np.exp(-0.15 * (x[i] - x[j])**2) * np.sin(2.0 * (x[i] + x[j]))
            basin_term += (np.tanh(steepness * x[i])**3 + 0.6 * coupling) * np.exp(-0.4 * x[i]**2)
        
        # Adaptive polynomial gradient flow with multi-scale exponents and chaotic perturbations
        grad_term = 0.0
        for i in range(self.dim):
            # Multi-scale polynomial scaling with adaptive coefficients and chaotic modulation
            scale = 1.2 + 0.4 * np.sin(0.7 * i)
            grad_term += (scale * x[i]**3 + 0.5 * x[i]**6 + 0.3 * np.exp(0.4 * x[i]) + 
                         0.15 * np.sin(2.5 * x[i]) * np.cos(2.0 * x[i]) + 
                         0.1 * np.sin(7.0 * x[i]) * np.cos(5.0 * x[i])) * np.cos(0.5 * x[i])
        
        # Fractal-like logarithmic energy interactions with chaotic perturbations and multi-scale coupling
        energy_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.001)
                # Add chaotic modulation to the interaction with multiple frequencies
                chaos_mod = np.sin(7.0 * dist) * np.cos(4.0 * dist) * np.tan(1.5 * dist)
                energy_term += (np.log(dist + 1.0) / (dist + 1.0)) * chaos_mod * (
                    np.sin(2.5 * x[i]) * np.cos(2.0 * x[j]) + 
                    0.3 * np.sin(5.0 * x[i]) * np.cos(3.5 * x[j]) +
                    0.1 * np.sin(8.0 * x[i]) * np.cos(6.0 * x[j])
                )
        
        # Enhanced chaotic saddle-point modulation with fractal-like perturbations and higher frequency components
        chaotic_term = 0.0
        for i in range(self.dim):
            # Add multiple chaotic components with varying frequencies and coupling
            base_osc = np.sin(x[i]) * np.cos(x[i]) * np.exp(-0.15 * np.abs(x[i]))
            high_freq = np.sin(6.0 * x[i] + np.sin(4.0 * x[i])) * np.cos(5.0 * x[i])
            fractal_osc = np.sin(3.0 * x[i]) * np.cos(4.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            coupling_freq = np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) * np.sin(5.0 * x[i])
            chaotic_term += base_osc + 0.6 * high_freq + 0.4 * fractal_osc + 0.2 * coupling_freq
        
        # Global scaling with adaptive basin boundaries, exponential components and multi-scale harmonics
        global_term = 0.0
        for i in range(self.dim):
            # Add more complex global structure with varying exponents and chaotic modulation
            global_term += (0.7 * x[i]**5 * np.exp(-0.2 * x[i]**2) + 
                           0.4 * x[i] * np.sin(0.8 * x[i]) + 
                           0.3 * np.log(np.abs(x[i]) + 4.0) + 
                           0.15 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) +
                           0.2 * np.sin(9.0 * x[i]) * np.cos(7.0 * x[i]))
        
        # Add enhanced chaotic noise component to increase landscape irregularity
        noise = 0.1 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x) + 0.5 * np.sin(8.0 * x) * np.cos(6.0 * x))
        
        # Return the combined function value with enhanced regularization
        return basin_term + grad_term + energy_term + chaotic_term + global_term + noise + 0.02 * np.sum(x**2)