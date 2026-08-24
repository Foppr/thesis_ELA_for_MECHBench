import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        quadratic = np.sum(x_norm**2) * (1.0 + 0.5 * np.sum(np.abs(x_norm)))
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        trig_term = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            amp = 1.0 + 0.3 * np.sin(i)
            trig_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2) + 0.4 * np.sin(3 * freq * x[i])
        
        # Create saddle points with hyperbolic tangent components and chaotic perturbations
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (np.tanh(x[i])**2 - 0.5 * np.tanh(2 * x[i])) * (1.0 + 0.2 * np.sin(7 * x[i]))
        
        # Nested structure with multiple local minima and chaotic scaling
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += 0.1 * np.sin(20 * x[i]) * np.cos(10 * x[i]) * np.exp(-0.1 * x[i]**2) * (1.0 + 0.1 * np.cos(13 * x[i]))
        
        # Add a complex interaction term between dimensions with chaotic coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.05 * (1.0 + 0.3 * np.sin(i * j))
                interaction_term += coupling * np.sin(5 * (x[i] + x[j])) * np.cos(3 * (x[i] - x[j])) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Add a chaotic perturbation term to increase landscape complexity
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += 0.2 * np.sin(17 * x[i]) * np.cos(11 * x[i]) * np.sin(13 * x[i])
        
        # Combine all terms with a global scaling factor
        result = quadratic + trig_term + saddle_term + nested_term + interaction_term + chaos_term
        
        # Add a non-linear scaling factor based on the norm of x
        result *= (1.0 + 0.3 * np.sum(np.abs(x_norm)) + 0.1 * np.sum(x_norm**4))
        
        return result