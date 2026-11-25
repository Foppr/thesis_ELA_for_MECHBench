import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize memory history buffer for each dimension
        self.memory = np.zeros((15, dim))
        # Fractal dimension scaling for spatial modulation
        self.fractal_dims = np.array([2.0 + 0.4 * np.sin(i * 0.6) for i in range(dim)])
        # Dynamical system parameters with increased chaos
        self.r_params = np.array([3.9 + 0.3 * np.sin(i * 0.4) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced discrete dynamical system with chaotic logistic map
        logistic = 0
        for i in range(self.dim):
            r = self.r_params[i % len(self.r_params)]
            # Use recent memory to influence current state with feedback
            mem_avg = np.mean(self.memory[:, i]) if np.any(self.memory[:, i]) else 0.0
            x_next = r * x[i] * (1 - x[i]) + 0.15 * mem_avg
            logistic += (x_next - x[i])**2
        
        # Memory-dependent potential wells with adaptive coefficients
        memory_potential = 0
        for i in range(self.dim):
            recent_history = self.memory[-4:, i]
            if len(recent_history) > 0:
                hist_mean = np.mean(recent_history)
                hist_std = np.std(recent_history)
                # Adaptive scaling based on history variance
                scale_factor = 1.0 + 0.5 * np.exp(-hist_std**2)
                memory_potential += scale_factor * (x[i] - hist_mean)**2
        
        # Fractal gradient modulation with enhanced dimensionality coupling
        fractal_grad = 0
        for i in range(self.dim):
            dim_frac = self.fractal_dims[i % len(self.fractal_dims)]
            # Enhanced gradient modification using multiple fractal dimensions
            grad_mod = 1.0 + 0.4 * np.sin(dim_frac * x[i]) * np.cos(0.5 * sum(x))
            fractal_grad += (x[i]**2 - 2*x[i] + 1) * grad_mod
        
        # Spatio-temporal coupling with time-varying attractors
        temporal = 0
        for i in range(self.dim):
            t_coeff = 1.0 + 0.3 * np.sin(0.6 * x[i]) * np.cos(0.4 * sum(x))
            # Enhanced temporal component with quartic terms
            temporal += (x[i]**4 - 6*x[i]**2 + 8) * t_coeff
        
        # Chaotic attractor modulation with improved sensitivity
        chaotic = 0
        for i in range(self.dim):
            r = 3.6 + 0.4 * np.sin(i * 0.5)
            x_prev = self.memory[-1, i] if len(self.memory) > 0 else x[i]
            attractor = np.sin(r * x_prev) + 0.1 * np.cos(2 * r * x_prev)
            chaotic += (x[i] - attractor)**2
        
        # Path-dependent fitness with cumulative history and momentum
        path_fitness = 0
        for i in range(self.dim):
            if len(self.memory) > 2:
                # Include momentum from previous steps
                momentum = np.mean(np.diff(self.memory[:, i][-3:]))
                path_fitness += np.sum((x[i] - self.memory[:-1, i])**2) + 0.5 * momentum**2
        
        # Combine all components with optimized weights for better balance
        weights = [0.25, 0.20, 0.18, 0.15, 0.12, 0.10]
        return (weights[0] * logistic + 
                weights[1] * memory_potential + 
                weights[2] * fractal_grad + 
                weights[3] * temporal + 
                weights[4] * chaotic + 
                weights[5] * path_fitness)