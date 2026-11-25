import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base exponential decay term with chaotic coefficient modulation and enhanced nonlinearity
        for i in range(self.dim):
            coeff = 0.5 * (1.0 + 0.3 * np.sin(7.0 * i)) * (1.0 + 0.1 * i**2)
            result += coeff * np.exp(-0.9 * (x[i] ** 2)) * (1.0 + 0.25 * i + 0.08 * x[i]**2 + 0.03 * x[i]**4)
        
        # Add multi-frequency trigonometric components with chaotic phase shifts and radial interaction
        for i in range(self.dim):
            freq = 5.0 * (i + 1) * (1.0 + 0.1 * np.cos(3.0 * i))
            phase = 0.6 * i + 0.2 * np.sin(4.0 * i)
            result += 0.4 * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] - phase) * np.exp(-0.25 * abs(x[i]))
        
        # Add radial symmetry component with chaotic frequency modulation and enhanced oscillation
        if self.dim >= 2:
            r = np.sqrt(x[0]**2 + x[1]**2)
            freq_mod = 8.0 + 2.0 * np.sin(0.5 * r)
            result += 0.7 * np.sin(freq_mod * r + 0.3 * r**2) * np.exp(-0.35 * r)
        
        # Add cross-dimensional interaction terms with chaotic coupling coefficients and polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.25 * (1.0 + 0.2 * np.sin(5.0 * (i + j))) * (1.0 + 0.05 * (i + j)**2)
                result += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2)) * (1.0 + 0.15 * (i + j))
        
        # Add asymmetric exponential terms with chaotic scaling and enhanced nonlinearity
        for i in range(self.dim):
            if x[i] > 0:
                scale = 0.4 * (1.0 + 0.2 * np.cos(2.0 * i))
                result += scale * np.exp(-0.55 * x[i]) * (1.0 + 0.35 * x[i]**2 + 0.07 * x[i]**4 + 0.02 * x[i]**6)
            else:
                scale = 0.35 * (1.0 + 0.15 * np.sin(3.0 * i))
                result += scale * np.exp(-0.65 * abs(x[i])) * (1.0 + 0.3 * x[i]**2 + 0.04 * x[i]**4 + 0.01 * x[i]**6)
        
        # Add high-frequency oscillatory component with chaotic amplitude modulation
        for i in range(self.dim):
            amp_mod = 0.3 * (1.0 + 0.25 * np.sin(8.0 * i))
            result += amp_mod * np.sin(40.0 * x[i]) * np.cos(35.0 * x[i]) * (1.0 + 0.15 * abs(x[i]))
        
        # Add polynomial interaction terms with chaotic degree scaling and enhanced coupling
        for i in range(min(self.dim, 5)):
            deg = 5.0 + 2.0 * np.sin(0.7 * i)
            coeff = 0.25 * (1.0 + 0.1 * np.cos(4.0 * i))
            result += coeff * (x[i] ** deg) * np.sin(x[i]) * (1.0 + 0.08 * i)
            
        # Add global modulation based on sum of squares with chaotic frequency and enhanced nonlinearity
        sum_squares = np.sum(x**2)
        freq_mod = 4.0 + 1.5 * np.sin(0.3 * sum_squares)
        result += 0.45 * np.exp(-0.25 * sum_squares) * np.sin(freq_mod * sum_squares + 0.15 * sum_squares**2)
        
        # Add boundary attraction term with chaotic penalty scaling
        for i in range(self.dim):
            penalty_scale = 0.3 * (1.0 + 0.2 * np.cos(6.0 * i))
            result += penalty_scale * (5.0 - abs(x[i]))**4
        
        # Add additional complexity with chaotic sine-cosine products and increased coupling
        for i in range(self.dim):
            for j in range(i+1, min(self.dim, i+4)):
                amp_mod = 0.2 * (1.0 + 0.15 * np.sin(7.0 * (i + j)))
                result += amp_mod * np.sin(3.0 * x[i]) * np.cos(4.0 * x[j]) * np.exp(-0.12 * (x[i]**2 + x[j]**2)) * (1.0 + 0.08 * (i + j))
        
        # Add chaotic radial component with higher frequency and stronger coupling
        if self.dim >= 3:
            r = np.sqrt(np.sum(x[:3]**2))
            freq_mod = 12.0 + 3.0 * np.sin(0.4 * r)
            result += 0.6 * np.sin(freq_mod * r) * np.cos(7.0 * r) * np.exp(-0.25 * r)
        
        # Add enhanced cross-dimensional coupling with chaotic polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.15 * (1.0 + 0.1 * np.sin(2.0 * (i + j)))
                result += coeff * (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j]) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
        
        # Add chaotic harmonic component with multi-scale frequency modulation
        for i in range(self.dim):
            freq = 15.0 * (1.0 + 0.3 * np.sin(0.8 * i)) * (i + 1)
            result += 0.18 * np.sin(freq * x[i]) * (1.0 + 0.2 * np.cos(freq * x[i])) * np.exp(-0.1 * abs(x[i]))
        
        return result