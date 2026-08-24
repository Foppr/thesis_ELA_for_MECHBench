import numpy as np

class ChaoticNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sigmoidal neural-like activation with chaotic modulation
        neural = np.sum(1.0 / (1.0 + np.exp(-3.0 * x_norm)) * np.sin(2.0 * x_norm) * np.cos(1.5 * x_norm))
        
        # Chaotic logistic map inspired interaction terms with dynamic coupling
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on input values
                coupling = 0.5 + 0.5 * np.sin(2.0 * (x_norm[i] + x_norm[j]))
                chaotic_interaction += coupling * np.exp(-0.1 * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(5.0 * (x_norm[i] - x_norm[j])) * np.cos(3.0 * (x_norm[i] + x_norm[j]))
        
        # Saddle point structure with hyperbolic tangent components
        saddle = np.sum(np.tanh(x_norm)**2 * np.sin(3.0 * x_norm) * np.cos(2.0 * x_norm))
        
        # Multi-scale oscillatory pattern with frequency modulation
        freq_mod = np.sum(np.sin(2.0 * x_norm) * np.cos(3.0 * x_norm) * np.sin(5.0 * x_norm) * np.cos(7.0 * x_norm))
        
        # Dynamic exponential decay with time-varying parameters
        decay = np.sum(np.exp(-0.5 * x_norm**2) * np.sin(4.0 * x_norm)**2 * np.cos(2.0 * x_norm)**2)
        
        # Cross-dimensional interaction with phase-shifted sine waves
        cross = np.sum(np.sin(x_norm[:-1] + x_norm[1:] + 0.7) * np.cos(x_norm[:-1] - x_norm[1:] - 0.4) * np.sin(2.0 * x_norm[:-1]) * np.cos(1.5 * x_norm[1:]))
        
        # Chaotic perturbation with multiple frequencies and amplitude modulation
        chaos_perturb = np.sum(np.sin(10.0 * x_norm) * np.cos(8.0 * x_norm) * np.sin(6.0 * x_norm) * np.cos(4.0 * x_norm) * np.exp(-0.3 * np.abs(x_norm)))
        
        # Shifted global optimum with non-linear transformation
        shift = 0.2 * np.sum((x_norm - 0.2)**4)
        
        # Combine all components with carefully tuned weights
        return 1.2 * neural + 1.8 * chaotic_interaction + 0.9 * saddle + 1.5 * freq_mod + 1.1 * decay + 0.7 * cross + 1.3 * chaos_perturb + 0.4 * shift