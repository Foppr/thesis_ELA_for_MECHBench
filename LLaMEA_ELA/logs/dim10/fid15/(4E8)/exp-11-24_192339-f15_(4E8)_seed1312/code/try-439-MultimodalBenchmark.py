import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize memory history buffer for each dimension
        self.memory = np.zeros((10, dim))
        # Fractal dimension scaling for spatial modulation
        self.fractal_dims = np.array([2.0 + 0.5 * np.sin(i * 0.5) for i in range(dim)])
        # Dynamical system parameters
        self.r_params = np.array([3.8 + 0.2 * np.sin(i * 0.3) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Discrete dynamical system component with logistic map
        logistic = 0
        for i in range(self.dim):
            r = self.r_params[i % len(self.r_params)]
            # Use recent memory to influence current state
            mem_avg = np.mean(self.memory[:, i]) if np.any(self.memory[:, i]) else 0.0
            x_next = r * x[i] * (1 - x[i]) + 0.1 * mem_avg
            logistic += (x_next - x[i])**2
        
        # Memory-dependent potential wells
        memory_potential = 0
        for i in range(self.dim):
            # Use history to modulate current potential
            recent_history = self.memory[-3:, i]
            if len(recent_history) > 0:
                hist_mean = np.mean(recent_history)
                hist_std = np.std(recent_history)
                memory_potential += (x[i] - hist_mean)**2 * np.exp(-hist_std**2)
        
        # Fractal gradient modulation
        fractal_grad = 0
        for i in range(self.dim):
            dim_frac = self.fractal_dims[i % len(self.fractal_dims)]
            # Modify gradient based on fractal dimension
            grad_mod = 1.0 + 0.3 * np.sin(dim_frac * x[i])
            fractal_grad += (x[i]**2 - 2*x[i] + 1) * grad_mod
        
        # Spatio-temporal coupling with time-varying coefficients
        temporal = 0
        for i in range(self.dim):
            t_coeff = 1.0 + 0.2 * np.sin(0.5 * x[i]) * np.cos(0.3 * sum(x))
            temporal += (x[i]**4 - 4*x[i]**2) * t_coeff
        
        # Chaotic attractor modulation
        chaotic = 0
        for i in range(self.dim):
            # Simple chaotic map: x_{n+1} = sin(r * x_n)
            r = 3.5 + 0.5 * np.sin(i * 0.4)
            x_prev = self.memory[-1, i] if len(self.memory) > 0 else x[i]
            attractor = np.sin(r * x_prev)
            chaotic += (x[i] - attractor)**2
        
        # Path-dependent fitness with cumulative history
        path_fitness = 0
        for i in range(self.dim):
            # Accumulate fitness based on previous evaluations
            if len(self.memory) > 1:
                path_fitness += np.sum((x[i] - self.memory[:-1, i])**2)
        
        # Combine all components with dynamic weights
        weights = [0.22, 0.20, 0.18, 0.17, 0.15, 0.08]
        return (weights[0] * logistic + 
                weights[1] * memory_potential + 
                weights[2] * fractal_grad + 
                weights[3] * temporal + 
                weights[4] * chaotic + 
                weights[5] * path_fitness)