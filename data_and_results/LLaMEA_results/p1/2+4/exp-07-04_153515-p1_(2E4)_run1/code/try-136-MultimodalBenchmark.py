import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        self.trig_freq = np.random.uniform(1.0, 3.0, dim)
        self.ridge_params = np.random.uniform(0.5, 2.0, dim)
        self.rotation_matrices = []
        for _ in range(3):
            rot = np.random.randn(dim, dim)
            self.rotation_matrices.append(np.linalg.qr(rot)[0])
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        f_val = 0.0
        
        # Logistic map chaotic component
        chaotic = np.zeros(self.dim)
        for i in range(self.dim):
            val = x[i]
            for _ in range(10):
                val = self.logistic_r[i] * val * (1 - val)
            chaotic[i] = val
        
        f_val += 0.2 * np.sum(chaotic**2)
        
        # Trigonometric periodic terms
        for i in range(self.dim):
            f_val += 0.15 * np.sin(self.trig_freq[i] * x[i]) * np.cos(self.trig_freq[i] * x[i])
        
        # Adaptive ridge structure with rotation
        for i, rot_mat in enumerate(self.rotation_matrices):
            rotated = rot_mat @ x
            ridge = np.sum((rotated * self.ridge_params)**2)
            f_val += 0.1 * np.exp(-0.1 * ridge) * np.sin(2 * ridge)
        
        # Cross-variable interaction with chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = np.sin(3 * chaotic[i]) * np.cos(2 * chaotic[j])
                f_val += 0.08 * np.sin(x[i]) * np.cos(x[j]) * mod * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Asymmetric polynomial with chaotic bias
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += 0.1 * x[i]**3 * np.sin(4 * x[i]) + 0.05 * x[i]**5 * np.cos(2 * x[i])
            else:
                f_val += 0.07 * x[i]**4 * np.cos(3 * x[i]) + 0.06 * x[i]**6 * np.sin(x[i])
        
        # Global sinusoidal modulation
        norm = np.sum(x**2)
        f_val += 0.1 * np.sin(0.5 * norm) * np.cos(0.3 * norm) * np.exp(-0.03 * norm)
        
        return f_val