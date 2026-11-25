import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize memory history buffer for each dimension
        self.memory = np.zeros((15, dim))
        # Fractal dimension scaling for spatial modulation
        self.fractal_dims = np.array([2.0 + 0.7 * np.sin(i * 0.6) for i in range(dim)])
        # Dynamical system parameters with quantum-like coupling
        self.r_params = np.array([3.9 + 0.3 * np.sin(i * 0.4) for i in range(dim)])
        # Quantum harmonic oscillator frequencies
        self.freqs = np.array([1.0 + 0.5 * np.cos(i * 0.3) for i in range(dim)])
        # Saddle-point modulation coefficients
        self.saddle_coeffs = np.array([0.8 + 0.4 * np.sin(i * 0.5) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillator component
        quantum = 0
        for i in range(self.dim):
            freq = self.freqs[i % len(self.freqs)]
            # Add quantum-like potential energy term
            quantum += 0.5 * freq**2 * x[i]**2 + 0.1 * np.sin(freq * x[i])
        
        # Discrete dynamical system component with logistic map and quantum coupling
        logistic = 0
        for i in range(self.dim):
            r = self.r_params[i % len(self.r_params)]
            # Use recent memory to influence current state with quantum phase
            mem_avg = np.mean(self.memory[:, i]) if np.any(self.memory[:, i]) else 0.0
            phase = np.sin(0.5 * x[i])
            x_next = r * x[i] * (1 - x[i]) + 0.1 * mem_avg + 0.05 * phase
            logistic += (x_next - x[i])**2
        
        # Memory-dependent potential wells with quantum tunneling effects
        memory_potential = 0
        for i in range(self.dim):
            # Use history to modulate current potential with quantum probability
            recent_history = self.memory[-4:, i]
            if len(recent_history) > 0:
                hist_mean = np.mean(recent_history)
                hist_std = np.std(recent_history)
                # Quantum tunneling effect: probability of being at a certain point
                prob_tunnel = np.exp(-hist_std**2) * (1.0 + 0.2 * np.sin(x[i]))
                memory_potential += (x[i] - hist_mean)**2 * prob_tunnel
        
        # Fractal gradient modulation with quantum scaling
        fractal_grad = 0
        for i in range(self.dim):
            dim_frac = self.fractal_dims[i % len(self.fractal_dims)]
            # Modify gradient based on fractal dimension and quantum frequency
            grad_mod = 1.0 + 0.4 * np.sin(dim_frac * x[i]) * np.cos(self.freqs[i])
            fractal_grad += (x[i]**3 - 3*x[i]) * grad_mod
        
        # Spatio-temporal coupling with time-varying coefficients and quantum phase
        temporal = 0
        for i in range(self.dim):
            t_coeff = 1.0 + 0.3 * np.sin(0.5 * x[i]) * np.cos(0.4 * sum(x))
            # Add quantum phase to temporal coupling
            phase = np.cos(0.3 * x[i])
            temporal += (x[i]**5 - 5*x[i]**3 + 4*x[i]) * t_coeff * phase
        
        # Chaotic attractor modulation with saddle-point dynamics
        chaotic = 0
        for i in range(self.dim):
            # Simple chaotic map: x_{n+1} = sin(r * x_n) with saddle-point modulation
            r = 3.6 + 0.4 * np.sin(i * 0.5)
            x_prev = self.memory[-1, i] if len(self.memory) > 0 else x[i]
            attractor = np.sin(r * x_prev)
            # Add saddle-point modulation
            saddle_mod = 1.0 + self.saddle_coeffs[i % len(self.saddle_coeffs)] * np.sin(x[i])
            chaotic += (x[i] - attractor)**2 * saddle_mod
        
        # Path-dependent fitness with cumulative history and quantum interference
        path_fitness = 0
        for i in range(self.dim):
            # Accumulate fitness based on previous evaluations with quantum interference
            if len(self.memory) > 1:
                diff = x[i] - self.memory[:-1, i]
                # Quantum interference pattern
                interference = np.prod([np.sin(0.2 * d) for d in diff])
                path_fitness += np.sum(diff**2) * (1.0 + 0.1 * interference)
        
        # Combine all components with dynamic weights
        weights = [0.18, 0.22, 0.15, 0.16, 0.17, 0.12]
        return (weights[0] * quantum + 
                weights[1] * logistic + 
                weights[2] * memory_potential + 
                weights[3] * fractal_grad + 
                weights[4] * temporal + 
                weights[5] * chaotic + 
                path_fitness)